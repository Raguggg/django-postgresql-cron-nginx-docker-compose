DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'postgres') THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE postgres');
   END IF;
END
$$;
