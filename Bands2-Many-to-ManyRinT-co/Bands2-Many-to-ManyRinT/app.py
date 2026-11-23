from flask import Flask, render_template, request, redirect, url_for, flash
from flask_admin.contrib.sqla import ModelView
from model import db, Bands, Members, Albums, Memberships, Artists, admin
import os

app = Flask(__name__)
CONFIG_TYPE = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
app.config.from_object(CONFIG_TYPE)
db.init_app(app)

with app.app_context():
    db.create_all()

admin.init_app(app)
admin.add_view(ModelView(Bands, db.session, category="Bands"))
admin.add_view(ModelView(Members, db.session, category="Members"))
admin.add_view(ModelView(Memberships, db.session, category="Members"))
admin.add_view(ModelView(Albums, db.session, category="Albums"))
admin.add_view(ModelView(Artists, db.session, category="Albums"))


@app.route("/")
def index():
    return render_template("index.html")


# BANDS
@app.route("/bands/view")
def view_by_band():
    bands = Bands.query.order_by(Bands.BandName).all()
    return render_template("display_by_band.html", bands=bands)


@app.route("/bands/view/<int:id>")
def view_band(id):
    band = Bands.query.get_or_404(id)
    return render_template("view_band.html", band=band)


@app.route("/bands/add", methods=["GET", "POST"])
def add_band():
    if request.method == "POST":
        try:
            band = Bands(
                BandName=(request.form.get("bandname") or "").strip(),
                FormedYear=request.form.get("formedyear") or None,
                HomeLocation=request.form.get("homelocation") or None,
            )
            if not band.BandName:
                flash("Band name is required.", "danger")
                return render_template("add_band.html")
            db.session.add(band)
            db.session.commit()
            flash(f"Added band: {band.BandName}", "success")
            return redirect(url_for("view_by_band"))
        except Exception:
            db.session.rollback()
            flash("Error adding band.", "danger")
    return render_template("add_band.html")


@app.route("/bands/edit/<int:id>", methods=["GET", "POST"])
def edit_band(id):
    band = Bands.query.get_or_404(id)
    if request.method == "POST":
        try:
            band.BandName = (request.form.get("bandname") or "").strip()
            band.FormedYear = request.form.get("formedyear") or None
            band.HomeLocation = request.form.get("homelocation") or None
            if not band.BandName:
                flash("Band name is required.", "danger")
                return render_template("edit_band.html", band=band)
            db.session.commit()
            flash(f"Updated band: {band.BandName}", "success")
            return redirect(url_for("view_by_band"))
        except Exception:
            db.session.rollback()
            flash("Error updating band.", "danger")
    return render_template("edit_band.html", band=band)


@app.route("/bands/delete/<int:id>")
def delete_band(id):
    band = Bands.query.get_or_404(id)
    try:
        db.session.delete(band)
        db.session.commit()
        flash(f"Deleted band: {band.BandName}", "success")
    except Exception:
        db.session.rollback()
        flash("Error deleting band.", "danger")
    return redirect(url_for("view_by_band"))


# MEMBERS
@app.route("/members/view")
def view_by_member():
    members = Members.query.order_by(Members.MemberName).all()
    return render_template("display_by_member.html", members=members)


@app.route("/members/view/<int:id>")
def view_member(id):
    member = Members.query.get_or_404(id)
    return render_template("view_member.html", member=member)


@app.route("/members/add", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        try:
            member = Members(
                MemberName=(request.form.get("membername") or "").strip(),
                MainPosition=request.form.get("mainposition") or None,
            )
            if not member.MemberName:
                flash("Member name is required.", "danger")
                return render_template("add_member.html", bands=Bands.query.all())
            db.session.add(member)
            db.session.commit()
            flash(f"Added member: {member.MemberName}", "success")
            return redirect(url_for("view_by_member"))
        except Exception:
            db.session.rollback()
            flash("Error adding member.", "danger")
    return render_template("add_member.html", bands=Bands.query.all())


@app.route("/members/edit/<int:id>", methods=["GET", "POST"])
def edit_member(id):
    member = Members.query.get_or_404(id)
    if request.method == "POST":
        try:
            member.MemberName = (request.form.get("membername") or "").strip()
            member.MainPosition = request.form.get("mainposition") or None
            if not member.MemberName:
                flash("Member name is required.", "danger")
                return render_template("edit_member.html", member=member)
            db.session.commit()
            flash(f"Updated member: {member.MemberName}", "success")
            return redirect(url_for("view_by_member"))
        except Exception:
            db.session.rollback()
            flash("Error editing member.", "danger")
    return render_template("edit_member.html", member=member)


@app.route("/members/delete/<int:id>")
def delete_member(id):
    member = Members.query.get_or_404(id)
    try:
        db.session.delete(member)
        db.session.commit()
        flash(f"Deleted member: {member.MemberName}", "success")
    except Exception:
        db.session.rollback()
        flash("Error deleting member.", "danger")
    return redirect(url_for("view_by_member"))


# BAND-MEMBER MEMBERSHIPS
@app.route("/memberships/add", methods=["GET", "POST"])
def add_membership():
    bands = Bands.query.order_by(Bands.BandName).all()
    members = Members.query.order_by(Members.MemberName).all()
    if request.method == "POST":
        try:
            band_id = request.form.get("bandid", type=int)
            member_id = request.form.get("memberid", type=int)
            band = db.session.get(Bands, band_id) if band_id else None
            member = db.session.get(Members, member_id) if member_id else None
            if not band or not member:
                flash("Please select a band and a member.", "danger")
            else:
                membership = Memberships(
                    BandID=band_id, MemberID=member_id,
                    Role=request.form.get("role") or None,
                    StartYear=request.form.get("startyear") or None,
                    EndYear=request.form.get("endyear") or None,
                )
                db.session.add(membership)
                db.session.commit()
                flash(f"Added {member.MemberName} to {band.BandName}.", "success")
                return redirect(url_for("view_by_band"))
        except Exception:
            db.session.rollback()
            flash("Error adding membership.", "danger")
    return render_template("add_membership.html", bands=bands, members=members)


@app.route("/memberships/edit/<int:id>", methods=["GET", "POST"])
def edit_membership(id):
    membership = Memberships.query.get_or_404(id)
    bands = Bands.query.order_by(Bands.BandName).all()
    members = Members.query.order_by(Members.MemberName).all()
    if request.method == "POST":
        try:
            band_id = request.form.get("bandid", type=int)
            member_id = request.form.get("memberid", type=int)
            band = db.session.get(Bands, band_id) if band_id else None
            member = db.session.get(Members, member_id) if member_id else None
            if not band or not member:
                flash("Please select a band and a member.", "danger")
            else:
                membership.BandID = band_id
                membership.MemberID = member_id
                membership.Role = request.form.get("role") or None
                membership.StartYear = request.form.get("startyear") or None
                membership.EndYear = request.form.get("endyear") or None
                db.session.commit()
                flash("Membership updated.", "success")
                return redirect(url_for("view_by_band"))
        except Exception:
            db.session.rollback()
            flash("Error editing membership.", "danger")
    return render_template("edit_membership.html", membership=membership, bands=bands, members=members)


@app.route("/memberships/delete/<int:id>")
def delete_membership(id):
    membership = Memberships.query.get_or_404(id)
    try:
        db.session.delete(membership)
        db.session.commit()
        flash("Membership removed.", "success")
    except Exception:
        db.session.rollback()
        flash("Error removing membership.", "danger")
    return redirect(url_for("view_by_band"))


# ALBUMS
@app.route("/albums/view")
def view_by_album():
    albums = Albums.query.order_by(Albums.AlbumTitle).all()
    return render_template("display_by_album.html", albums=albums)


@app.route("/albums/view/<int:id>")
def view_album(id):
    album = Albums.query.get_or_404(id)
    return render_template("view_album.html", album=album)


@app.route("/albums/add", methods=["GET", "POST"])
def add_album():
    if request.method == "POST":
        title = (request.form.get("albumtitle") or "").strip()
        year = request.form.get("releaseyear") or None
        if not title:
            flash("Album title is required.", "danger")
        else:
            try:
                album = Albums(AlbumTitle=title, ReleaseYear=int(year) if year else None)
                db.session.add(album)
                db.session.commit()
                flash(f"Added album: {title}. Now connect it to one or more bands.", "success")
                return redirect(url_for("add_artist", album_id=album.AlbumID))
            except Exception:
                db.session.rollback()
                flash("Error adding album. Check the release year.", "danger")
    return render_template("add_album.html")


# ARTISTS is the Band <-> Album association table
@app.route("/artists/add", methods=["GET", "POST"])
@app.route("/artist/add", methods=["GET", "POST"])
def add_artist():
    bands = Bands.query.order_by(Bands.BandName).all()
    albums = Albums.query.order_by(Albums.AlbumTitle).all()
    selected_album_id = request.args.get("album_id", type=int)
    if request.method == "POST":
        band_id = request.form.get("bandid", type=int)
        album_id = request.form.get("albumid", type=int)
        band = db.session.get(Bands, band_id) if band_id else None
        album = db.session.get(Albums, album_id) if album_id else None
        if not band or not album:
            flash("Please select both a band and an album.", "danger")
        elif Artists.query.filter_by(BandID=band_id, AlbumID=album_id).first():
            flash(f"{band.BandName} is already connected to {album.AlbumTitle}.", "warning")
        else:
            try:
                db.session.add(Artists(BandID=band_id, AlbumID=album_id))
                db.session.commit()
                flash(f"Connected {band.BandName} to {album.AlbumTitle}.", "success")
                return redirect(url_for("view_album", id=album.AlbumID))
            except Exception:
                db.session.rollback()
                flash("Unable to create that band/album connection.", "danger")
    return render_template("add_artist.html", bands=bands, albums=albums, selected_album_id=selected_album_id)


@app.route("/artists/edit/<int:id>", methods=["GET", "POST"])
@app.route("/artist/edit/<int:id>", methods=["GET", "POST"])
def edit_artist(id):
    credit = Artists.query.get_or_404(id)
    bands = Bands.query.order_by(Bands.BandName).all()
    albums = Albums.query.order_by(Albums.AlbumTitle).all()
    if request.method == "POST":
        band_id = request.form.get("bandid", type=int)
        album_id = request.form.get("albumid", type=int)
        band = db.session.get(Bands, band_id) if band_id else None
        album = db.session.get(Albums, album_id) if album_id else None
        duplicate = Artists.query.filter(
            Artists.BandID == band_id,
            Artists.AlbumID == album_id,
            Artists.ArtistID != credit.ArtistID,
        ).first()
        if not band or not album:
            flash("Please select both a band and an album.", "danger")
        elif duplicate:
            flash("That band is already connected to that album.", "warning")
        else:
            try:
                old_album_id = credit.AlbumID
                credit.BandID = band_id
                credit.AlbumID = album_id
                db.session.commit()
                flash("Band/album connection updated.", "success")
                return redirect(url_for("view_album", id=album_id))
            except Exception:
                db.session.rollback()
                flash("Error updating the band/album connection.", "danger")
    return render_template("edit_artist.html", artist=credit, bands=bands, albums=albums)


@app.route("/artists/delete/<int:id>")
@app.route("/artist/delete/<int:id>")
def delete_artist(id):
    credit = Artists.query.get_or_404(id)
    album_id = credit.AlbumID
    try:
        db.session.delete(credit)
        db.session.commit()
        flash("Band/album connection removed.", "success")
    except Exception:
        db.session.rollback()
        flash("Error removing the band/album connection.", "danger")
    return redirect(url_for("view_album", id=album_id))


if __name__ == "__main__":
    app.run(debug=True)
