from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=.\SQLEXPRESS;"
    "DATABASE=ExpenseTracker;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form["amount"]
    category = request.form["category"]
    item = request.form["item"]

    cursor.execute(
        "INSERT INTO expenses (amount, category, item) VALUES (?, ?, ?)",
        (amount, category, item)
    )
    conn.commit()

    return redirect("/")


@app.route("/view")
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    return render_template("view.html", expenses=rows)


@app.route("/total")
def total_spent():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()
    total = result[0] if result[0] else 0

    return f"<h2>Total Spent: {total} birr</h2><a href='/'>Back</a>"


@app.route("/category")
def spending_by_category():
    cursor.execute("""
        SELECT category, SUM(amount) 
        FROM expenses 
        GROUP BY category
    """)
    rows = cursor.fetchall()

    output = "<h2>Spending by Category</h2>"
    for row in rows:
        output += f"<p>{row[0]}: {row[1]} birr</p>"

    output += "<br><a href='/'>Back</a>"
    return output


if __name__ == "__main__":
    app.run(debug=True)