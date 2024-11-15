from abc import ABC, abstractmethod
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd


class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, events):
        pass


class PDFReportGenerator(ReportGenerator):
    def generate(self, events):
        doc = SimpleDocTemplate("events_report.pdf")
        styles = getSampleStyleSheet()
        elements = []
        for event in events:
            # Accede a los atributos del objeto 'event' directamente
            event_details = f"Nombre del evento: {event.name}, Fecha del evento: {event.event_date}, Lugar del evento: {event.venue.name}"
            elements.append(Paragraph(event_details, styles["BodyText"]))
            elements.append(Spacer(1, 12))
        doc.build(elements)

class ExcelReportGenerator(ReportGenerator):
    def generate(self, events):
        df = pd.DataFrame([(event.name, event.event_date.replace(tzinfo=None), event.venue.name) for event in events], columns=["Event", "Date", "Venue"])
        df.to_excel("events_report.xlsx", index=False)