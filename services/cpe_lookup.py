import requests


def get_cpe(product):

    try:

        url = (
            "https://services.nvd.nist.gov/rest/json/cpes/2.0"
            f"?keywordSearch={product}"
        )

        response = requests.get(url, timeout=20)

        data = response.json()

        if "products" not in data:
            return None

        if len(data["products"]) == 0:
            return None

        return data["products"][0]["cpe"]["cpeName"]

    except Exception as e:

        print("CPE Error:", e)

        return None