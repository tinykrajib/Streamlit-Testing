

import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import extra_streamlit_components as stx

from streamlit_geolocation import streamlit_geolocation


import math
import pandas as pd

class tlt:
    def __init__(self):
        pass
    
    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # Convert decimal degrees to radians 
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r

    def tlt_zone(self, lat1, lon1, df_res_CSV):
        # Check for None values and handle appropriately
        if lat1 is None or lon1 is None:
            raise ValueError("Latitude or Longitude cannot be None")

        try:
            lat1 = float(lat1)
            lon1 = float(lon1)
        except ValueError as e:
            raise ValueError(f"Invalid latitude or longitude value: {e}")
        """
        Calculate the distance from a point to all points in a CSV file
        and print the top 5 closest points with their respective zones.
        """
        # Read the CSV file into a DataFrame
        df_res = pd.read_csv(df_res_CSV)


        # Check if the coordinates are within Thailand's bounding box
        if 5.6 <= lat1 <= 20.4 and 97.3 <= lon1 <= 105.6: 
            
            # Calculate distances and add them as a new column
            df_res['distance'] = df_res.apply(lambda row: self.haversine_distance(lat1, lon1, row['lat'], row['lng']), axis=1)
            
            # Sort the DataFrame by distance and display the top 5 closest points
            closest_points = df_res.sort_values(by='distance').head(5)
            # print(closest_points)
            
            # Print the zone of the closest point
            closest_zone = df_res.sort_values(by='distance').iloc[0]['tlt_area']

            count_EV_min = int( df_res [ df_res['tlt_area'] == closest_zone ]['avg_event'].min() )
            count_EV_max = int(  df_res [ df_res['tlt_area'] == closest_zone ]['avg_event'].max() )
            yearly_avg_payment = df_res [ df_res['tlt_area'] == closest_zone ]['yearly_avg_payment'].mean()
            weekly_avg_payment = df_res [ df_res['tlt_area'] == closest_zone ]['weekly_avg_payment'].mean()

            # print("zone:", closest_zone)
        else:
            closest_zone = "พื้นที่อยู่นอกประเทศไทย"
            count_EV_min = 0
            count_EV_max = 0 
            yearly_avg_payment = 0
            weekly_avg_payment = 0
          
        return closest_zone, count_EV_min, count_EV_max, weekly_avg_payment, yearly_avg_payment
    
    def zone_detail(self, closest_zone, count_EV_min, count_EV_max):

        # 1. พื้นที่ "พลังงานเงินทอง" (Gold Power) #00ab20

        # 2.  พื้นที่ "พลังงานเติบโต" (Growth Power) #4cd100

        # 3.  พื้นที่  "พลังงานเสริม" (Boost Power) #f2dd20

        # 4.  พื้นที่ "พลังงานพื้นฐาน" (Basic Power)  #fa9600;

            # Display a color block with text

    
        if closest_zone== 'gold_power':
          
            html_color_ = f"""
            <div style="display: flex; align-items: center;">
                <div style="width: 50px; height: 50px; background-color: #00ab20; margin-right: 10px;"></div>
                <div style="font-size: 20px; color: #dcdcdc;">พื้นที่ "พลังงานเงินทอง" (Gold Power) &#11088 &#11088 &#11088</div>
            </div>
                <ul>
                    <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรเฉลี่ยอยู่ในระหว่าง  {count_EV_min} ถึง {count_EV_max} คันต่อสัปดาห์โดยเฉลี่ย  </li>
                    <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่ที่มีความต้องการใช้บริการสูงมาก และมีแนวโม้วที่จะเป็นทำเลที่มีโอกาสสร้างรายได้สูงและมีอัตราการคืนทุนที่รวดเร็ว</li>
                </ul>
                <p>คำเตือน : ผู้ลงทุนควรทำความเข้าใจลักษณะสินค้าเงื่อนไขผลตอบแทนและความเสี่ยงก่อนตัดสินใจลงทุน ผลการดำเนินงานในอดีต มิได้เป็นสิ่งยืนยันถึงผลการดำเนินงานในอนาคต</p>
            """
            


        elif closest_zone== 'growth_power':

         
            html_color_ = f"""
            <hr>
            <div style="display: flex; align-items: center;">
                <div style="width: 50px; height: 50px; background-color: #4cd100; margin-right: 10px;"></div>
                <div style="font-size: 20px; color: #dcdcdc;">พื้นที่ "พลังงานเติบโต" (Growth Power) &#11088 &#11088</div>
            </div>
                <ul>
                    <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรเฉลี่ยอยู่ในระหว่าง  {count_EV_min} ถึง {count_EV_max} คันต่อสัปดาห์โดยเฉลี่ย  </li>
                    <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่ที่มีศักยภาพในการเติบโตสูง เป็นทำเลที่มีแนวโน้มว่าความต้องการใช้บริการจะเพิ่มขึ้นในอนาคต ทำให้มีโอกาสในการขยายธุรกิจและสร้างผลตอบแทนในระยะยาว</li>
                </ul>
                <p>คำเตือน : ผู้ลงทุนควรทำความเข้าใจลักษณะสินค้าเงื่อนไขผลตอบแทนและความเสี่ยงก่อนตัดสินใจลงทุน ผลการดำเนินงานในอดีต มิได้เป็นสิ่งยืนยันถึงผลการดำเนินงานในอนาคต</p>
            """
            
        
        elif closest_zone== 'boost_power':

            html_color_ = f"""
            <hr>
            <div style="display: flex; align-items: center;">
                <div style="width: 50px; height: 50px; background-color: #f2dd20; margin-right: 10px;"></div>
                <div style="font-size: 20px; color: #dcdcdc;">พื้นที่  "พลังงานเสริม" (Boost Power) &#11088 </div>
            </div>
                <ul>
                    <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรเฉลี่ยอยู่ในระหว่าง  {count_EV_min} ถึง {count_EV_max} คันต่อสัปดาห์โดยเฉลี่ย  </li>
                    <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่ที่มีกิจกรรมเฉพาะตัว เป็นทำเลที่สามารถดึงดูดลูกค้าเฉพาะกลุ่มได้ และสามารถสร้างรายได้เสริมจากการให้บริการอื่นๆ</li>
                </ul>
                <p>คำเตือน : ผู้ลงทุนควรทำความเข้าใจลักษณะสินค้าเงื่อนไขผลตอบแทนและความเสี่ยงก่อนตัดสินใจลงทุน ผลการดำเนินงานในอดีต มิได้เป็นสิ่งยืนยันถึงผลการดำเนินงานในอนาคต</p>
            """
          
        elif closest_zone == 'basic_power':
        
            html_color_ = f"""
                <hr>
                <div style="display: flex; align-items: center;">
                    <div style="width: 50px; height: 50px; background-color: #fa9600; margin-right: 10px;"></div>
                    <div style="font-size: 20px; color: #dcdcdc;">พื้นที่ "พลังงานพื้นฐาน" (Basic Power) </div>
                </div>
                    <ul>
                        <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรอยู่ในระหว่าง {count_EV_min} ถึง {count_EV_max} คันต่อสัปดาห์โดยเฉลี่ย </li>
                        <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่อื่นๆ ที่ไม่เข้าข่ายในกลุ่มข้างต้น เป็นทำเลที่มีความต้องการใช้บริการอาจจะน้อยกว่ากลุ่มอื่นๆ แต่ก็ยังมีความสำคัญในการสร้างเครือข่ายสถานีชาร์จให้ครอบคลุม</li>
                    </ul>
                <p>คำเตือน : ผู้ลงทุนควรทำความเข้าใจลักษณะสินค้าเงื่อนไขผลตอบแทนและความเสี่ยงก่อนตัดสินใจลงทุน ผลการดำเนินงานในอดีต มิได้เป็นสิ่งยืนยันถึงผลการดำเนินงานในอนาคต</p>
                """
   
        else :
            html_color_ = """ 
            """
        
        return html_color_
    
        # st.markdown(html_color_block, unsafe_allow_html=True)

    def zone_detail_all(self):

        # 1. พื้นที่ "พลังงานเงินทอง" (Gold Power) #00ab20

        # 2.  พื้นที่ "พลังงานเติบโต" (Growth Power) #4cd100

        # 3.  พื้นที่  "พลังงานเสริม" (Boost Power) #f2dd20


        # 4.  พื้นที่ "พลังงานพื้นฐาน" (Basic Power)  #fa9600;

            # Display a color block with text

     

        html_color_block = """
        <hr>
        <h2>คำอธิบาย</h2>
        <p>การแบ่งกลุ่มสถานีชาร์จรถยนต์ไฟฟ้าตามศักยภาพในการสร้างผลตอบแทน จะช่วยให้เราสามารถวางแผนการลงทุนและบริหารจัดการสถานีชาร์จได้อย่างมีประสิทธิภาพมากขึ้น โดยเราสามารถตั้งชื่อกลุ่มได้ดังนี้ค่ะ</p>
        <div style="display: flex; align-items: center;">
            <div style="width: 50px; height: 50px; background-color: #00ab20; margin-right: 10px;"></div>
            <div style="font-size: 20px; color: #dcdcdc;">พื้นที่ "พลังงานเงินทอง" (Gold Power) &#11088 &#11088 &#11088</div>
         </div>
            <ul>
                <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรเฉลี่ยอยู่ในระหว่าง 124 ถึง 239 คันในแต่ละสัปดาห์  </li>
                <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่ที่มีความต้องการใช้บริการสูงมาก และมีแนวโม้วที่จะเป็นทำเลที่มีโอกาสสร้างรายได้สูงและมีอัตราการคืนทุนที่รวดเร็ว</li>
            </ul>
        <div style="display: flex; align-items: center;">
            <div style="width: 50px; height: 50px; background-color: #4cd100; margin-right: 10px;"></div>
            <div style="font-size: 20px; color: #dcdcdc;">พื้นที่ "พลังงานเติบโต" (Growth Power) &#11088 &#11088</div>
        </div>
            <ul>
                <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรเฉลี่ยอยู่ในระหว่าง 61 - 117 คันในแต่ละสัปดาห์ </li>
                <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่ที่มีศักยภาพในการเติบโตสูง เป็นทำเลที่มีแนวโน้มว่าความต้องการใช้บริการจะเพิ่มขึ้นในอนาคต ทำให้มีโอกาสในการขยายธุรกิจและสร้างผลตอบแทนในระยะยาว</li>
            </ul>
        <div style="display: flex; align-items: center;">
            <div style="width: 50px; height: 50px; background-color: #f2dd20; margin-right: 10px;"></div>
            <div style="font-size: 20px; color: #dcdcdc;">พื้นที่  "พลังงานเสริม" (Boost Power) &#11088 </div>
        </div>
            <ul>
                <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรเฉลี่ยอยู่ในระหว่าง 30 - 60 คันในแต่ละสัปดาห์ </li>
                <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่ที่มีกิจกรรมเฉพาะตัว เป็นทำเลที่สามารถดึงดูดลูกค้าเฉพาะกลุ่มได้ และสามารถสร้างรายได้เสริมจากการให้บริการอื่นๆ</li>
            </ul>
        <div style="display: flex; align-items: center;">
            <div style="width: 50px; height: 50px; background-color: #fa9600; margin-right: 10px;"></div>
            <div style="font-size: 20px; color: #dcdcdc;">พื้นที่ "พลังงานพื้นฐาน" (Basic Power) </div>
        </div>
            <ul>
                <li>เป็นพื้นที่ที่มี ปริมาณรถยนต์ไฟฟ้าสัญจรเฉลี่ยอยู่ในระหว่าง 2 - 29 คันในแต่ละสัปดาห์ </li>
                <li>ลักษณะ: เป็นสถานีชาร์จที่ตั้งอยู่ในพื้นที่อื่นๆ ที่ไม่เข้าข่ายในกลุ่มข้างต้น เป็นทำเลที่มีความต้องการใช้บริการอาจจะน้อยกว่ากลุ่มอื่นๆ แต่ก็ยังมีความสำคัญในการสร้างเครือข่ายสถานีชาร์จให้ครอบคลุม</li>
            </ul>
        <p>คำเตือน : ผู้ลงทุนควรทำความเข้าใจลักษณะสินค้าเงื่อนไขผลตอบแทนและความเสี่ยงก่อนตัดสินใจลงทุน ผลการดำเนินงานในอดีต มิได้เป็นสิ่งยืนยันถึงผลการดำเนินงานในอนาคต</p>
        """
        return html_color_block
        

    
    def get_province(self, lat1, lon1):

        # Check for None values and handle appropriately
        if lat1 is None or lon1 is None:
            raise ValueError("Latitude or Longitude cannot be None")

        try:
            lat1 = float(lat1)
            lon1 = float(lon1)

        except ValueError as e:
            raise ValueError(f"Invalid latitude or longitude value: {e}")
        
        # Read the CSV file into a DataFrame
        # df_res = pd.read_csv(df_res_CSV)
       
        
        province = "ไม่พบจังหวัดในประเทศไทย"
        if 5.6 <= lat1 <= 20.4 and 97.3 <= lon1 <= 105.6: 
            # Calculate distances and add them as a new column
            dist = 9999999
            PATH = "resources/thai_area.csv"
            df_thai_area = pd.read_csv(PATH)

            for i in range(len(df_thai_area)):
                lat_pvt = df_thai_area['lat'].loc[i]
                lng_pvt = df_thai_area['lng'].loc[i]

                # Check if the coordinates are within Thailand's bounding box
            
                if dist > self.haversine_distance(lat1, lon1, lat_pvt,lng_pvt ):
                    dist = self.haversine_distance(lat1, lon1, lat_pvt,lng_pvt )
                    province = df_thai_area['province'].loc[i]
                    district = df_thai_area['district'].loc[i]

        else:
            province = "ไม่พบจังหวัดในประเทศไทย"
            district = "--"
           
        
        return province, district
    
    def get_current_location(self):

        location = streamlit_geolocation()
        return location["latitude"], location["longitude"]
        # st.write(location)
    def calculate_payback_period(self, capital_cost, annual_benefit):
        """
        Calculate the payback period given the capital cost and annual benefit.

        Parameters:
        capital_cost (float): The initial capital cost.
        annual_benefit (float): The annual benefit or savings.

        Returns:
        float: The payback period in years.
        """
        if annual_benefit == 0:
            formatted_number = "{:.2f}".format(float('inf'))
            return formatted_number   # If annual benefit is zero, payback period is infinite
        else:
            formatted_number = "{:.2f}".format(capital_cost / annual_benefit)
            return formatted_number 

if __name__ == '__main__':

    # Example usage
    tlt_instance = tlt()
    lat1 = 37.7749   # Example latitude
    lon1 = -122.4194 # Example longitude
    df_res_CSV = 'path_to_your_csv_file.csv' # Path to your CSV file

    tlt_instance.tlt_zone(lat1, lon1, df_res_CSV)



