from datetime import datetime
from auctioncore.models import Auction, Participants

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
import random


def is_time_out():
    for a in Auction.objects.all():
        if a.end_date < datetime.now():
            a.is_active = False
            a.is_done = True
            a.save()
            auction_done(a)


def auction_done(a):
    owner_user = a.owner
    part_user = Participants.objects.filter(auction=a, bet=a.last_bet)
    if part_user:
        part_user = part_user[0].user
        # auction_success(owner_user, part_user)
    else:
        # auction_fail(owner_user)
        pass
#
# def auction_success(owner, winner):
#     o_email_address = [owner.email]
#     w_email_address = [winner.email]
#
#     o_email = EmailMessage()
#
#     o_email.subject = 'Поздравляем, ваш аукцион состоялся!'
#
#     o_email.from_email = "E-Auction.kg <eauction.kg@gmail.com>"
#     o_email.to = o_email_address
#     o_email.attach(content='owner', mimetype="text/html")
#     o_email.send()
#
#     w_email = EmailMessage()
#
#     w_email.subject = 'Поздравляем, вы выиграли аукцион состоялся!'
#
#     w_email.from_email = "E-Auction.kg <eauction.kg@gmail.com>"
#     w_email.to = w_email_address
#     w_email.attach(content='owner', mimetype="text/html")
#     w_email.send()
#
#
# def auction_fail(owner):
#     o_email_address = [owner.email]
#
#     o_email = EmailMessage()
#
#     o_email.subject = 'К сожалению, ваш аукцион не состоялся!'
#
#     o_email.from_email = "E-Auction.kg <eauction.kg@gmail.com>"
#     o_email.to = o_email_address
#     o_email.attach(content='owner', mimetype="text/html")
#     o_email.send()
