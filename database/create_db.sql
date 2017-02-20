CREATE USER mailreader WITH PASSWORD 'mailreaderpw';

\c accounts

GRANT SELECT ON ALL TABLES IN SCHEMA public TO mailreader;
