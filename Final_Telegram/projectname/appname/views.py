from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from final_telegram import TelegramScraper

def index(request,contact):
    
    scraper = TelegramScraper()
    scraped_data = scraper.scrape_telegram_user(contact)
    return JsonResponse(scraped_data)