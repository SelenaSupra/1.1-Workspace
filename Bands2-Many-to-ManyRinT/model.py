from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

db = SQLAlchemy()
admin = Admin()


class Bands(db.Model):
    __tablename__ = "bands"

    BandID = db.Column(db.Integer, primary_key=True)
    BandName = db.Column(db.String(80), nullable=False)
    FormedYear = db.Column(db.Integer)
    HomeLocation = db.Column(db.String(80))

    memberships = db.relationship(
        "Memberships", back_populates="band", cascade="all, delete-orphan"
    )
    artists = db.relationship(
        "Artists", back_populates="band", cascade="all, delete-orphan"
    )


class Members(db.Model):
    __tablename__ = "members"

    MemberID = db.Column(db.Integer, primary_key=True)
    MemberName = db.Column(db.String(80), nullable=False)
    MainPosition = db.Column(db.String(80))

    memberships = db.relationship(
        "Memberships", back_populates="member", cascade="all, delete-orphan"
    )


class Memberships(db.Model):
    __tablename__ = "memberships"

    MembershipID = db.Column(db.Integer, primary_key=True)
    BandID = db.Column(db.Integer, db.ForeignKey("bands.BandID"), nullable=False)
    MemberID = db.Column(db.Integer, db.ForeignKey("members.MemberID"), nullable=False)
    Role = db.Column(db.String(80))
    StartYear = db.Column(db.Integer)
    EndYear = db.Column(db.Integer)

    band = db.relationship("Bands", back_populates="memberships")
    member = db.relationship("Members", back_populates="memberships")


class Albums(db.Model):
    __tablename__ = "albums"

    AlbumID = db.Column(db.Integer, primary_key=True)
    AlbumTitle = db.Column(db.String(80), nullable=False)
    ReleaseYear = db.Column(db.Integer)

    artists = db.relationship(
        "Artists", back_populates="album", cascade="all, delete-orphan"
    )


class Artists(db.Model):
    """Association object connecting one band to one album."""
    __tablename__ = "artists"
    __table_args__ = (
        db.UniqueConstraint("BandID", "AlbumID", name="uq_artist_band_album"),
    )

    ArtistID = db.Column(db.Integer, primary_key=True)
    BandID = db.Column(db.Integer, db.ForeignKey("bands.BandID"), nullable=False)
    AlbumID = db.Column(db.Integer, db.ForeignKey("albums.AlbumID"), nullable=False)

    band = db.relationship("Bands", back_populates="artists")
    album = db.relationship("Albums", back_populates="artists")