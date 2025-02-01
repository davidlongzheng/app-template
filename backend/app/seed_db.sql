-- Insert sample users
INSERT INTO users (email, name, hashed_password)
VALUES
    ('admin@example.com', 'Admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyNiAYMxRRQvea'),
    ('user1@example.com', 'User 1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyNiAYMxRRQvea'),
    ('user2@example.com', 'User 2', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyNiAYMxRRQvea');

-- Insert sample movies
INSERT INTO movies (title, released, rating)
VALUES
    ('The Shawshank Redemption', 1994, 9.3),
    ('The Godfather', 1972, 9.2),
    ('The Dark Knight', 2008, 9.0),
    ('Pulp Fiction', 1994, 8.9),
    ('Forrest Gump', 1994, 8.8);
