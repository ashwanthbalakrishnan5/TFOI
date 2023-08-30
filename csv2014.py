import csv
from poll.models import BoothData2014

with open("2014BoothData.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        polling_booth = BoothData2014(
            polling_booth_number=row["Polling Booth Number"],
            polling_booth_name=row["Polling Booth Name"],
            winner_2014=row["Winner- 2014 "],
            first_runner_up_other_than_INC_and_BJP=row[
                "1st Runner up other than INC and BJP"
            ],
            margin_percent=row["Margin (%)"],
            margin=row["Margin"],
            total=row["Total"],
            BJP_votes=row["BJP - Votes"],
            BJP_percent_vote=row["BJP- % vote"],
            INC_votes=row["INC- Votes"],
            INC_percent_votes=row["INC- % votes"],
            Dadarao_Kisansro_Uikey=row["Dadarao Kisansro Uikey"],
            Deashmukh_Nilesh_Madhukarrao=row["Deashmukh Nilesh Madhukarrao"],
            Sandeep_Dilip_Kale=row["Sandeep Dilip Kale"],
            Prashant_Gokuldasji_Kathane=row["Prashant Gokuldasji Kathane"],
            Dnyaneshwar_Narayan_Maddavi=row["Dnyaneshwar Narayan Maddavi"],
            Arvind_Shamrao_Lillore=row["Arvind Shamrao Lillore"],
            Arun_Ajabrao_Pachare=row["Arun Ajabrao Pachare"],
            Topale_Rupchand_Bhuraji=row["Topale Rupchand Bhuraji"],
            Tarachand_Sonbaji_Nehare=row["Tarachand Sonbaji Nehare"],
            Dilip_Shamraoji_Potfode=row["Dilip Shamraoji Potfode"],
            Nikose_Wasudeo_Shamrao=row["Nikose Wasudeo Shamrao"],
            Sanjay_Dhondbaji_Tule=row["Sanjay Dhondbaji Tule"],
            wapnil_Alias_Bala_Rameshrao_Jagtap=row[
                "wapnil Alias Bala Rameshrao Jagtap"
            ],
            NOTA=row["NOTA"],
            no_of_tendered_votes=row["No. of tendered votes"],
            no_of_votes_gotten_by_3rd_parties=row["No of Votes gotten by 3rd parties"],
        )
        polling_booth.save()
