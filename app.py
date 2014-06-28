from flask import Flask
app = Flask(__name__)

@app.route('/pollutants')
def get_polutants():
    return 'Pollutants'

@app.route('/sites')
def get_sites():
    return 'Sites'

@app.route('/sites/<site_id>/pollutants')
def get_pollutants_by_sites_with_query():
    return 'Pollutants by site'

@app.route('/sites/<site_id>/pollutants/<pollutant_id>')
def get_polutants_by_sites_and_pollutant_with_query():
    return 'Pollutants by site and pollutant'
    

if __name__ == '__main__':
    app.run()