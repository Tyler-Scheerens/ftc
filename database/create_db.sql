

CREATE EXTENSION pgcrypto;

CREATE USER mailreader WITH PASSWORD 'mailreaderpw';

GRANT ALL PRIVILEGES ON DATABASE accounts to mailreader;

CREATE TABLE virtual_domain (
    id serial PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE virtual_mailbox (
    id serial PRIMARY KEY,
    domain_id INTEGER NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    maildir TEXT NOT NULL,
    created TIMESTAMP WITH TIME ZONE DEFAULT now(),
    FOREIGN KEY (domain_id) REFERENCES virtual_domain(id) ON DELETE CASCADE
);

CREATE TABLE virtual_alias (
    id serial PRIMARY KEY,
    domain_id INTEGER NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    FOREIGN KEY (domain_id) REFERENCES virtual_domain(id) ON DELETE CASCADE
);

CREATE TABLE transport (
    domain TEXT NOT NULL,
    gid INTEGER UNIQUE NOT NULL,
    transport TEXT NOT NULL
);


INSERT INTO accounts.virtual_domain
(name)
VALUES
('example.com'),
('hostname.example.com');


INSERT INTO accounts.virtual_mailbox
(domain_id, password, email)
VALUES
(1, crypt('ecnrypted_password',gen_salt('bf',5)), 'email1@example.com'),
(1, crypt('ecnrypted_password',gen_salt('bf',5)), 'email2@example.com');


INSERT INTO accounts.virtual_alias
(domain_id, source, destination)
VALUES
(1, 'alias@example.com', 'email1@example.com');

