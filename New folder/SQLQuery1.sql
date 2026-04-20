USE ExpenseTracker;
GO

CREATE TABLE expenses (
    id INT IDENTITY(1,1) PRIMARY KEY, -- auto-increment ID
    amount FLOAT NOT NULL,            -- how much money was spent
    category VARCHAR(100) NOT NULL,   -- Food, Transport, Bills, etc.
    item VARCHAR(255),                -- optional item name
    date DATE DEFAULT GETDATE()       -- date of expense, defaults to today
);
GO

SELECT * FROM expenses;