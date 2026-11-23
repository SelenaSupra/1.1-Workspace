# Bands 2 — Band/Album Many-to-Many

This project extends Bands 2 with a many-to-many relationship between Bands and Albums. The existing `Artists` model is the association table: each row connects one `BandID` to one `AlbumID`. The database enforces one connection per band/album pair.

## Relationship design

- `Bands` has many `Artists` association rows.
- `Albums` has many `Artists` association rows.
- Each `Artists` row belongs to exactly one Band and one Album.
- `Artists` is intentionally retained as the association model name from the starter project.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` if needed.
4. Run `flask run --debug`.

The default database name is now `bands2_many_to_many.db`, so your original `bands2.db` is left untouched. The app creates the new database tables on first run. If you choose to point `DB_NAME` at an existing old database, back it up first; `db.create_all()` does not migrate existing tables.

## Using the app

1. Add an album from Albums → Add an Album.
2. Add the first band connection from the redirect, or use Albums → Add Band/Album Collaboration.
3. To add another collaborating band to the same album, add another collaboration and select that same album.
4. View connections from either the Bands or Albums pages. Use each connection's Actions menu to edit or delete that individual association.

## Git workflow / pull request

Create a feature branch before making changes, commit the work, push the branch to your fork, and open a pull request against the instructor repository. This downloaded copy does not automatically create or push a GitHub branch or pull request.
