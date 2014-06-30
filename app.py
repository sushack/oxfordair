from flask import Flask, jsonify, render_template
from models import Pollutant, PollutantCollection, PollutantData, PollutantDataCollection
from models import Site, SiteCollection
from data_import import SingleSiteCSVParser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pollutants')
def get_pollutants():
    data = [{"id": p.id,
                    "name": p.name,
                    "unit": p.unit} for p in pollutant_collection.objects()]
    return jsonify({"pollutants": data})

@app.route('/sites')
def get_sites():
    data = [{"id": s.id,
                    "name": s.name,
                    "pollutants": [p.id for p in s.available_pollutants]} for s in site_collection.objects()]
    print data
    return jsonify({"sites": data})

@app.route('/sites/<site_id>/pollutants')
def get_pollutants_by_sites_with_query(site_id):
    site = site_collection.get_by_id(site_id)

    if site is None:
        abort(404)

    site_pollution_data = pollutant_data_collection.find(site=site)
    
    data = [{"value": d.value,
             "datetime": d.timestamp,
             "pollutant_id": d.pollutant.id
            } for d in site_pollution_data]
    # print data
    return jsonify({"pollutant_data": data})

@app.route('/sites/<site_id>/pollutants/<pollutant_id>')
def get_polutants_by_sites_and_pollutant_with_query(site_id, pollutant_id):
    site = site_collection.get_by_id(site_id)
    pollutant = pollutant_collection.get_by_id(pollutant_id)

    site_pollution_data = pollutant_data_collection.find(site=site, pollutant=pollutant)
    
    data = [{"value": d.value,
             "datetime": d.timestamp,
             "pollutant_id": d.pollutant.id
            } for d in site_pollution_data]
    # print data
    return jsonify({"pollutant_data": data})
    

if __name__ == '__main__':
    site_collection = SiteCollection()
    pollutant_collection = PollutantCollection()
    pollutant_data_collection = PollutantDataCollection()
    SingleSiteCSVParser("data/OX_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)
    SingleSiteCSVParser("data/OX8_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)
    
    app.run(debug=True, host="0.0.0.0")
