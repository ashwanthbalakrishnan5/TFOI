import csv
from poll.models import BoothData2019

with open("2019BoothData.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        polling_booth = BoothData2019(
            polling_booth_number=row["Polling Booth Number"],
            polling_booth_name=row["Polling Booth Name"],
            winner_2019=row["Winner- 2019"],
            margin_percent=row["Margin %"],
            margin=row["Margin"],
            total_voters=row["Total Voters"],
            BJP_votes=row["BJP- Votes"],
            BJP_percent_votes=row["BJP- % votes"],
            INC_votes=row["INC- Votes"],
            INC_percent_votes=row["INC- % Votes"],
            Adv_Chandrashekar_Dongre=row["Adv. Chandrashekar Dongre"],
            Topale_Rupachand=row["Topale Rupachand"],
            Rahul_Parasanji_Tayde=row["Rahul Parasanji Tayde"],
            Sanjay_Ambadas_Wankhede=row["Sanjay Ambadas Wankhede"],
            Avinash_Suresh_Badhiye=row["Avinash Suresh Badhiye"],
            Deepak_M_Madavi=row["Deepak M. Madavi"],
            Dilip_Shamraoji_Potfode=row["Dilip Shamraoji Potfode"],
            Vilas_Vinayakrao_Kailuke=row["Vilas Vinayakrao Kailuke"],
            NOTA=row["NOTA"],
            no_of_votes_got_by_3rd_parties=row["No of Votes got by 3rd parties"],
            BJP_booth_strength=row["BJP booth strength"],
            INC_booth_strength=row["INC booth strength"],
        )
        polling_booth.save()
