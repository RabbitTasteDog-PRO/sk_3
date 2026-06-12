import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut
from pathlib import Path
import time

st.title("전기차 충전소 사용량 지도")

base_path = Path(__file__).parent.parent
csv_path = base_path / "Data" / "test_data.csv"
coords_path = base_path / "Data" / "coords.csv"

df = pd.read_csv(csv_path, encoding="cp949")

df["address"] = df["광역지자체"] + " " + df["시군구"] + " 대한민국"

st.dataframe(df.head())

geolocator = Nominatim(
    user_agent="ev_charger_dashboard",
    timeout=10
)

def get_lat_lon(address):
    try:
        location = geolocator.geocode(address)

        if location:
            return location.latitude, location.longitude

    except (GeocoderUnavailable, GeocoderTimedOut):
        st.warning(f"좌표 조회 실패: {address}")

    return None, None


if coords_path.exists():
    coord_df = pd.read_csv(coords_path)
    st.success("저장된 좌표 파일을 불러왔습니다.")
else:
    st.info("좌표 파일이 없어 처음 1회 좌표를 조회합니다.")

    unique_addresses = df["address"].drop_duplicates().tolist()

    coord_list = []
    progress = st.progress(0)

    for i, address in enumerate(unique_addresses):
        lat, lon = get_lat_lon(address)

        coord_list.append({
            "address": address,
            "lat": lat,
            "lon": lon
        })

        progress.progress((i + 1) / len(unique_addresses))
        time.sleep(1)

    coord_df = pd.DataFrame(coord_list)
    coord_df.to_csv(coords_path, index=False, encoding="utf-8-sig")

    st.success("좌표 파일 저장 완료")

merged_df = df.merge(coord_df, on="address", how="left")

map_df = merged_df.dropna(subset=["lat", "lon"])

st.subheader("지역별 위치 지도")

if map_df.empty:
    st.error("지도에 표시할 좌표가 없습니다.")
else:
    st.map(map_df, latitude="lat", longitude="lon")
    st.dataframe(map_df[["광역지자체", "시군구", "lat", "lon"]])