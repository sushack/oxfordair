from flask import Flask, jsonify
from models import Pollutant, PollutantCollection, PollutantData, PollutantDataCollection
from models import Site, SiteCollection
from data_import import SingleSiteCSVParser

app = Flask(__name__)

@app.route('/pollutants')
def get_pollutants():
    data = [{"id": p.id,
                    "name": p.name,
                    "unit": p.unit} for p in pollutant_collection.objects()]
    return jsonify({"pollutants": data})

@app.route('/sites')
def get_sites():
    return 'Sites'

@app.route('/sites/<site_id>/pollutants')
def get_pollutants_by_sites_with_query():

    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    frequency = request.args.get('frequency', '')
    summary = request.args.get('summary', '')
    
    return 'Pollutants by site'

@app.route('/sites/<site_id>/pollutants/<pollutant_id>')
def get_polutants_by_sites_and_pollutant_with_query():
    return 'Pollutants by site and pollutant'
    

if __name__ == '__main__':
    site_collection = SiteCollection()
    pollutant_collection = PollutantCollection()
    pollutant_data_collection = PollutantDataCollection()
    SingleSiteCSVParser("data/OX_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)
    SingleSiteCSVParser("data/OX8_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)
    
    app.run(debug=True)
