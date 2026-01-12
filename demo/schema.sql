-- Placeholder schema for demo purposes only
-- The full production schema is not included

CREATE TABLE leads (
    id INTEGER PRIMARY KEY,
    name TEXT,
    status TEXT,
    created_at TEXT
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    lead_id INTEGER,
    content TEXT,
    sent_at TEXT
);
