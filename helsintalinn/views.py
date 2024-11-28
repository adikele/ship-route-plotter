from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
imports from bend detection
'''
#import megastar_helper_bends 
import pandas
import geopandas
import matplotlib.pyplot as plt
from geodatasets import get_path  ### used for getting the background earth
import pyproj

from shapely import Point, LineString
import shapely as shapely

# from covidplots:
import pandas as pd
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.shortcuts import render, redirect, get_object_or_404

#from .forms import CountriesSelectForm
from .forms import CountrySelectForm
# from .utilities import *
import random
import os
from django.conf import settings
from  .megastar_helper_bends import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def select_country_form(request):
# def select_route_form(request):
    global x
    global y
    form = CountrySelectForm()
    if request.method == "POST":
        form = CountrySelectForm(request.POST)
        if form.is_valid():
            #cd = form.cleaned_data
            #country_sel = cd.get("selected_country")
            #df = pd.read_csv(DATA_FILE)
            #df_meri = pd.read_csv("oship")
            #file_ = open(os.path.join(settings.BASE_DIR, 'ship2.csv'))
            df_meri = pd.read_csv(os.path.join(settings.BASE_DIR, 'ship2.csv'))
            main ()


            fig = create_figure(x, y)

            response = django.http.HttpResponse(content_type="image/png")
            FigureCanvas(fig).print_png(response)
            return response

    else:
        # this is the case when user sees the form for the first time
        form = CountrySelectForm()
    return render(request, "helsintalinn/country_form.html", {"form": form})


def calculate_bearing_2(long1, lat1, long2, lat2):
    geodesic = pyproj.Geod(ellps='WGS84')
    fwd_azimuth,back_azimuth,distance = geodesic.inv(long1, lat1, long2, lat2)
    if fwd_azimuth < 0:
        fwd_azimuth += 360
    return (fwd_azimuth)

def calculate_bearing_3(long1, lat1, long2, lat2):
    geodesic = pyproj.Geod(ellps='WGS84')
    fwd_azimuth,back_azimuth,distance = geodesic.inv(long1, lat1, long2, lat2)
    return (distance)

def main ():
    #df_meri = pandas.read_csv('opensource_ship3_100rows.csv')
    df_meri = pd.read_csv('ship2.csv')

    # step 2:
    df_meri ['intermediate_points'] = [Point(xy) for xy in zip(df_meri['long'], df_meri['lat'] )]

    gdf_meri = geopandas.GeoDataFrame(df_meri, geometry='intermediate_points', crs="EPSG:4326")
    print (gdf_meri.head())


    gdf_meri["next_lat"] = gdf_meri["lat"].shift(-1)
    gdf_meri["next_long"] = gdf_meri["long"].shift(-1)



    gdf_meri["current_bearing"] = gdf_meri.apply(
            lambda row: calculate_bearing_2(
                row.long,
                row.lat,
                row.next_long,
                row.next_lat,
            ),
            axis=1,
        )

    gdf_meri["distance"] = gdf_meri.apply(
            lambda row: calculate_bearing_3(
                row.long,
                row.lat,
                row.next_long,
                row.next_lat,
            ),
            axis=1,
        )

    # gdf_meri['intermediate_points'] = zip(gdf_meri.lat, gdf_meri.long)

    gdf1_meri = gdf_meri[gdf_meri["ship"]=="Megastar"]  
    print ("Megastar...")
    print ("Megastar...")
    print (gdf1_meri.head())
    print ("Megastar END")

    gdf2_meri = gdf_meri[gdf_meri["ship"]=="Star"]
    print ("Star...")
    print ("Star...")
    print (gdf2_meri.head())
    print ("Star END")
    
    #df_routeline = helper_bend.set_routeline_s_bend_length_new(df_routeline)   # from väylä
    #gdf2_meri = megastar_helper_bends.set_routeline_s_bend_length_new(gdf2_meri)
    gdf2_meri = set_routeline_s_bend_length_new(gdf2_meri)

    print ("Star AFTER detection...")
    print ("Star AFTER detection...")
    print (gdf2_meri.head)

    world = geopandas.read_file(get_path("naturalearth.land"))

    ax = world.clip([20.0, 60.0, 25.5, 70.3]).plot(color="green", edgecolor="black") 

    gdf1_meri.plot(ax=ax, color="red")  # Megastar

    gdf2_meri.plot(ax=ax, color="brown")  # Star

    plt.show()

'''
        file = request.FILES['files']
        obj = File.objects.create(
            file=file
        )

        path = file.file
        df = pd.read_excel(path)


def select_country_form(request):
    global x
    global y
    form = CountrySelectForm()
    if request.method == "POST":
        form = CountrySelectForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            country_sel = cd.get("selected_country")
            df = pd.read_csv(DATA_FILE)

            list_countries, list_cases = fetch_home_continent_data(df, country_sel)
            dict_continent = dict(zip(list_countries, list_cases))
            list_countries_random = random_countries(list_countries, country_sel)
            dict_fivecountries = fetch_five_countries_data(
                dict_continent, country_sel, list_countries_random
            )

            x = dict_fivecountries.keys()
            y = dict_fivecountries.values()

            fig = create_figure(x, y)

            response = django.http.HttpResponse(content_type="image/png")
            FigureCanvas(fig).print_png(response)
            return response

    else:
        # this is the case when user sees the form for the first time
        form = CountrySelectForm()
    return render(request, "covidplots/country_form.html", {"form": form})
'''