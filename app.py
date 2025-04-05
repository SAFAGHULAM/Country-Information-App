import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        # Increased timeout to 30 seconds
        response = requests.get(url, timeout=30, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            country_data = data[0]
            name = country_data["name"]["common"]
            capital = country_data["capital"][0] if "capital" in country_data else "N/A"
            population = country_data["population"]
            area = country_data["area"]
            currency = country_data["currencies"]
            region = country_data["region"]
            return name, capital, population, area, currency, region
        else:
            return None
    
    except requests.exceptions.Timeout:
        st.error("The request timed out. Please try again later.")
        return None
    
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Country Information App")
    
    country_name = st.text_input("Enter a country name:")
    
    if country_name:
        country_data = fetch_country_data(country_name)
        
        if country_data:
            name, capital, population, area, currency, region = country_data
            
            st.subheader("Country Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} km²")
            st.write(f"**Currency:** {list(currency.keys())[0]}")
            st.write(f"**Region:** {region}")
        else:
            st.error("Country not found. Please try again.")
            
if __name__ == "__main__":
    main()


