import os
import dotenv 
from supabase import Client, create_client
from model.Featured import Featured

class SuperbaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        self.supabase: Client = None

    def create_client(self):
        if self.supabase is None:
            self.supabase = create_client(self.SUPABASE_URL,self.SUPABASE_KEY)
            

    def featured(self) -> list[Featured]:

        if self.supabase is None:
            self.create_client()

        response = self.supabase.table("featuared").select("*").execute()

        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                featured_data.append(
                    Featured(
                        title=featured_item["title"],
                        image=featured_item["image"],
                        url=featured_item["url"]
                    )
                )

        return featured_data