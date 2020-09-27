#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from sqlalchemy.orm import backref, session
from flask_migrate import Migrate
import sys
from sqlalchemy import func
import datetime
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)
db.create_all()
# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))
    date = db.Column(db.TIMESTAMP)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def __init__(self,name,city,state,address,phone,genres,facebook_link):
        self.name = name
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.genres = genres
        self.facebook_link = facebook_link


class Artist(db.Model):
    __tablename__ = 'Artist'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    venue_id = db.relationship('Venue', backref=backref('Artist', order_by=id))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def __init__(self,name,phone,genres,facebook_link,website):
        
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.genres = genres
        self.website = website
        self.facebook_link = facebook_link
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#----------------------------------------------------------------------------#
# Filters
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  # num_shows should be aggregated based on number of upcoming shows per venue.
    data = Venue.query.all()
    return render_template('pages/venues.html', areas=data);

@app.route('/venues/<search>', methods=['POST'])
def search_venues(search):
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
    results = []
    search = request.form.get('search_term','')
    
    if search:
        results = Venue.query.filter_by(name=search).all()
        count = db.session.query(func.count(Venue.artist_id)).scalar()        
    if  not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        response={
            "count": count,
            "data": [{
              "id": results.id,
              "name": results.name,
              "num_upcoming_shows":count,
            }]
            }
        return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
    venue = Venue.query.get(venue_id) 
    artist = Artist.query.get(venue_id)
    rows = db.session.query(func.count(Venue.artist_id)).scalar()
    row_count = db.session.query(func.count(artist.venue_id))
    date = datetime.datetime.now()
    data1={
        "id": artist.id,
        "name": venue.name,
        "genres":artist.genres,
        "address": venue.address,
        "city": venue.city,
        "state": venue.state,
        "phone": venue.phone,
        "website": artist.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,
        "past_shows": [{
        "artist_id": artist,
        "artist_name": artist.name,
        "artist_image_link": artist.image_link,
        "start_time": str(venue.date)
      }],
      "upcoming_shows": db.session.query(Venue.artist_id).filter(Venue.date>=date),
      "past_shows_count": db.session.query(Venue.artist_id).filter(Venue.date.between(format_datetime(str(date)), format_datetime(str(date)))),
      "upcoming_shows_count": db.session.query(Venue.artist_id).filter(Venue.date <= date),}
    data2={
        "id": artist.id,
        "name": venue.name,
        "genres":artist.genres,
        "address": venue.address,
        "city": venue.city,
        "state": venue.state,
        "phone": venue.phone,
        "website": artist.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,
        "past_shows": [{
        "artist_id": artist,
        "artist_name": artist.name,
        "artist_image_link": artist.image_link,
        "start_time": str(venue.date)
      }],
      "upcoming_shows":db.session.query(Venue.artist_id).filter(Venue.date>=date),
      "past_shows_count": db.session.query(Venue.artist_id).filter(Venue.date.between(format_datetime(str(date)), format_datetime(str(date)))),
      "upcoming_shows_count": db.session.query(Venue.artist_id).filter(Venue.date <= date),
      }
    data3={
        "id": artist.id,
        "name": venue.name,
        "genres":artist.genres,
        "address": venue.address,
        "city": venue.city,
        "state": venue.state,
        "phone": venue.phone,
        "website": artist.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,
        "past_shows": [{
        "artist_id": artist,
        "artist_name": artist.name,
        "artist_image_link": artist.image_link,
        "start_time": str(venue.date)
      }],
      "upcoming_shows": db.session.query(Venue.artist_id).filter(Venue.date >= date),
      "past_shows_count": db.session.query(Venue.artist_id).filter(Venue.date.between(format_datetime(str(date)), format_datetime(str(date)))),
      "upcoming_shows_count": db.session.query(Venue.artist_id).filter(Venue.date <= date),}
      
    data = list(filter(lambda d: d['id'] == venue_id, [data1, data2, data3]))[0]
    return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
    error = False
    try:
        name = request.form['name']
        city = request.form['city']
        state = request.form['state']
        address = request.form['address']
        phone = request.form['phone']
        genres = request.form['genres']
        facebook_link = request.form['facebook_link']
        venue = Venue(name,city,state,address,phone,genres,facebook_link)
        db.session.add(venue)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
    if error:
        return render_template('errors/500.html')
    else:
        flash('Venue ' + request.form['name'] + ' was successfully listed!')
#  on successful db insert, flash success
#  TODO: on unsuccessful db insert, flash an error instead.
#  e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
#  see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to del 
  # delete a record. Handle cases where the session commit could fail.
    try:
        venue = Venue.query.filter(Venue.id==venue_id).one_or_none()
        venue.session.delete()
        venue.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
    return render_template('pages/home.html')

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  artists = Artist.query.all()
  data=[{
    "id": artist.id,
    "name": artist.name,
  } for artist in artists]
  return render_template('pages/artists.html', artists=data)
  
@app.route('/artists/<search>', methods=['POST'])
def search_artists(search):
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".

  results = []
  search = request.form.get('search_term','')

  if search:
      rows = db.session.query(func.count(search)).scalar()
      artist = Artist.query.filter_by(name=search).all()   
  if  not artist:
      flash('No results found!')
      return redirect('/artists')
  else:
      response={
        "count": rows,
        "data": [{
          "id": artist.id,
          "name": artist.name,
          "num_upcoming_shows": Venue.artist_id,
        }]
      }
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):  
    
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
    date = datetime.datetime.now()
    artists = Artist.query.get(artist_id)
    venue = Venue.query.get(artist_id)
    rows = venue.query.filter_by(format_datetime(str(venue.date))>=format_datetime(str(date))).count()
    past_shows = db.session.query(func.count(Venue.artist_id)).filter(Venue.date <= date)
    past_shows_count = db.session.query(func.count(past_shows)).scalar() 
    upcoming_shows = Venue.query.filter_by(format_datetime(str(venue.date))>=format_datetime(str(date))).all()
    upcoming_shows_count = db.session.query(func.count(upcoming_shows)).scalar()

    
    data1={
    "id": artists.id,
    "name": artists.name,
    "genres": artists.genres,
    "city": artists.city,
    "state": artists.state,
    "phone": artists.phone,
    "website": artists.website,
    "facebook_link": artists.facebook_link,
    "seeking_venue": venue.seeking_talent,
    "seeking_description": venue.seeking_description,
    "image_link": artists.image_link,
    "past_shows": [{
      "venue_id": past_shows.id,
      "venue_name": past_shows.name,
      "venue_image_link": past_shows.image_link,
      "start_time": str(past_shows.date),
      }],
    "upcoming_shows": [{
        "venue_id": upcoming_shows.id,
        "venue_name": upcoming_shows.name,
        "venue_image_link": upcoming_shows.image_link,
        "start_time": str(upcoming_shows.date),
        }],
    "past_shows_count": past_shows_count,
    "upcoming_shows_count": upcoming_shows,
    }
    data2={
    "id":artists.id,
    "name": artists.name,
    "genres": artists.genres,
    "city": artists.city,
    "state": artists.state,
    "phone": artists.phone,
    "facebook_link": artists.website,
    "seeking_venue": venue.seeking_talent,
    "image_link": artists.image_link,
     "past_shows": [{
      "venue_id": venue.id,
      "venue_name": venue.name,
      "venue_image_link": venue.image_link,
      "start_time": str(venue.date),
    }],
    "upcoming_shows": [{
        "venue_id": upcoming_shows.id,
        "venue_name": upcoming_shows.name,
        "venue_image_link": upcoming_shows.image_link,
        "start_time": str(upcoming_shows.date)
        }],
    "past_shows_count": past_shows_count,
    "upcoming_shows_count": upcoming_shows,
    }
    data3={
      "id": artists.id,
      "name": artists.name,
      "genres": artists.genres,
      "city": artists.city,
      "state": artists.state,
      "phone": artists.phone,
      "seeking_venue": venue.seeking_talent,
      "image_link": artists.image_link,
      "past_shows": [{
          "venue_id": past_shows.id,
          "venue_name": past_shows.name,
          "venue_image_link": past_shows.image_link,
          "start_time": str(past_shows.date)
          }],
      "upcoming_shows": [{
       "venue_id": upcoming_shows.id,
        "venue_name": upcoming_shows.name,
        "venue_image_link": upcoming_shows.image_link,
        "start_time": str(upcoming_shows.date),
      }, {
       "venue_id": upcoming_shows.id,
        "venue_name": upcoming_shows.name,
        "venue_image_link": upcoming_shows.image_link,
        "start_time": str(upcoming_shows.date)
      }, {
       "venue_id": upcoming_shows.id,
        "venue_name": upcoming_shows.name,
        "venue_image_link": upcoming_shows.image_link,
        "start_time": str(upcoming_shows.date)
      }],
      "past_shows_count": past_shows_count,
      "upcoming_shows_count": str(rows),
      }
    data = list(filter(lambda d: d['id'] == artist_id, [data1, data2, data3]))[0]   
    return render_template('pages/show_artist.html', artist=data)
    

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
    return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
      
    venue = Venue.query.filter_by(id=venue_id).first()
    artist = Artist.query.filter_by(venue_id=venue_id).first()
    form = VenueForm()

    venue={
      "id": venue.id,
      "name": venue.name,
      "genres": venue.genres,
      "address": venue.address,
      "city": venue.city,
      "state": venue.state,
      "phone": venue.phone,
      "website": venue.website,
      "facebook_link": artist.website,
      "seeking_talent": venue.seeking_talent,
      "seeking_description": venue.seeking_description,
      "image_link": seeking_description.image_link
      }
    
  # TODO: populate form with values from venue with ID <venue_id>
    return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  
    try:
        venue = Venue.query.filter_by(id=venue_id).first()
        venue.name = request.form['name']
        venue.city = request.form['city']
        venue.state = request.form['state']
        venue.address = request.form['address']
        venue.phone = request.form['phone']
        venue.genres = request.form['genres']
        venue.facebook_link = request.form['facebook_link']
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
    if error:
        return render_template('errors/500.html')
    # on successful db insert, flash success
    else:
        flash('Venue ' + request.form['name'] + ' was successfully listed!')
        return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
    try:
        name = request.form['name']
        city = request.form['city']
        state = request.form['state']
        genres = request.form['genres']
        phone = request.form['phone']
        facebook_link = request.form['facebook_link']
        artist = Artist(name,phone,genres,facebook_link)
        venue = Venue(city,state)
        db.session.add(artist,venue)
        db.session.commit()
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
    if error:
        return render_template('errors/500.html')
    # on successful db insert, flash success
    else:
        flash('Artist ' + request.form['name'] + ' was successfully listed!')
        return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  # num_shows should be aggregated based on number of upcoming shows per venue.
  venue = Venue.query.all()
  artist = Artist.query.all()
  data=[{
    "venue_id": venue[0].id,
    "venue_name": venue[0].name,
    "artist_id": venue[0].artist_id,
    "artist_name": artist[0].query.get(str(venue[0].artist_id)),
    "artist_image_link": venue[0].image_link,
    "start_time": str(venue[0].date)
  }, {
     "venue_id": venue[1].id,
    "venue_name": venue[1].name,
    "artist_id": venue[1].artist_id,
    "artist_name": artist[1].query.get(str(venue[1].artist_id)),
    "artist_image_link": venue[1].image_link,
    "start_time": str(venue[1].date)
  }, {
    "venue_id": venue[2].id,
    "venue_name": venue[2].name,
    "artist_id": venue[2].artist_id,
    "artist_name": artist[2].query.get(str(venue[2].artist_id)),
    "artist_image_link": venue[2].image_link,
    "start_time": str(venue[2].date)
  }, {
    "venue_id": venue[3].id,
    "venue_name": venue[3].name,
    "artist_id": venue[3].artist_id,
    "artist_name": artist[3].query.get(str(venue[3].artist_id)),
    "artist_image_link": venue[3].image_link,
    "start_time": str(venue[3].date)
  }, {
    "venue_id": venue[4].id,
    "venue_name": venue[4].name,
    "artist_id": venue[4].artist_id,
    "artist_name": artist[4].query.get(str(venue[4].artist_id)),
    "artist_image_link": venue[4].image_link,
    "start_time": str(venue[4].date)
  }]
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  
  # on successful db insert, flash success
  flash('Show was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
