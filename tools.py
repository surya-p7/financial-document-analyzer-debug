## Importing libraries and files
import os
from dotenv import load_dotenv
from crewai_tools import tool, SerperDevTool
# # tools.py - CORRECTED CODE
# from crewai_tools.tools.base_tool import tool
# from crewai_tools.tools.serper_dev_tool import SerperDevTool
from pypdf import PdfReader

load_dotenv()

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
@tool('Financial Document Reader')
def read_data_tool(path: str) -> str:
    """Tool to read all text data from a PDF file from a given path."""
    try:
        reader = PdfReader(path)
        full_report = ""
        for page in reader.pages:
            content = page.extract_text() or ""
            # Clean and format the financial document data
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report
    except Exception as e:
        return f"Error reading PDF file: {e}"

## Creating Investment Analysis Tool (Placeholder)
class InvestmentTool:
    def analyze_investment_tool(financial_document_data):
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool (Placeholder)
class RiskTool:
    def create_risk_assessment_tool(financial_document_data):
        return "Risk assessment functionality to be implemented"