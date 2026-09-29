from abc import ABC, abstractmethod
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from src.data_access.models import ProspectiveSite

class SiteRepositoryInterface(ABC):
    @abstractmethod
    def insert_sites(self, sites_data: List[Dict[str, Any]]) -> None:
        pass
        
    @abstractmethod
    def get_all_sites(self) -> List[ProspectiveSite]:
        pass

class SiteRepository(SiteRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def insert_sites(self, sites_data: List[Dict[str, Any]]) -> None:
        # Fetch existing site names to prevent duplicates
        existing_sites = {s[0] for s in self.session.query(ProspectiveSite.site_name).all()}
        
        new_sites = []
        for data in sites_data:
            if data.get('site_name') not in existing_sites:
                new_sites.append(ProspectiveSite(**data))
                
        if new_sites:
            self.session.add_all(new_sites)
            self.session.commit()
        
    def get_all_sites(self) -> List[ProspectiveSite]:
        return self.session.query(ProspectiveSite).all()
