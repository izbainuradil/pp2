-- 1. Pattern search
CREATE OR REPLACE FUNCTION search_contacts(p text)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM contacts
    WHERE name ILIKE '%' || p || '%'
       OR phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


-- 2. Pagination
CREATE OR REPLACE FUNCTION get_contacts_page(lim INT, off INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM contacts
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;


-- 3. Count function (extra example)
CREATE OR REPLACE FUNCTION count_contacts()
RETURNS INT AS $$
DECLARE total INT;
BEGIN
    SELECT COUNT(*) INTO total FROM contacts;
    RETURN total;
END;
$$ LANGUAGE plpgsql;