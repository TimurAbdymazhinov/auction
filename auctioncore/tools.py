from datetime import datetime
from auctioncore.models import Auction, Participants

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
import random


def is_time_out():
    for a in Auction.objects.filter(is_active=True):
        if a.end_date < datetime.now():
            auction_done(a)


def auction_done(a):
    a.is_active = False

    owner_user = a.owner
    part_user = Participants.objects.filter(auction=a, bet=a.last_bet)
    if part_user:
        a.is_done = True

        part_user = part_user[0].user
        auction_success(owner_user, part_user, a)
    else:
        auction_fail(owner_user)
        a.is_done = False


def auction_success(owner, winner, a):
    o_email_address = [owner.email]
    w_email_address = [winner.email]

    o_email = EmailMessage()

    o_email.subject = 'Поздравляем, ваш аукцион состоялся!'

    o_email.from_email = "E-Auction.kg <eauction.kg@gmail.com>"
    o_email.to = o_email_address
    m = \
        '''
        <h3>Ваш аукцион состоялся</h3>
        <p>Победитель: {}</p>
        <p>Номер телефона: {}</p>
        <p>email: {}</p>
        <p>Последняя ставка победителя: {}</p>
        '''.format(winner.first_name + ' ' + winner.last_name, winner.profile.phone, winner.email, a.last_bet)
    o_email.attach(content=m, mimetype="text/html")
    o_email.send()

    w_email = EmailMessage()

    w_email.subject = 'Поздравляем, вы выиграли аукцион состоялся!'
    m = \
        '''
        <h3>Ваш вы выиграли аукцион {}</h3>
        <p>Аукционист: {}</p>
        <p>Номер телефона: {}</p>
        <p>email: {}</p>
        <p>Последняя ставка победителя: {}</p>
        '''.format(a.title, owner.first_name + ' ' + owner.last_name, owner.profile.phone, owner.email, a.last_bet)

    w_email.from_email = "E-Auction.kg <eauction.kg@gmail.com>"
    w_email.to = w_email_address
    w_email.attach(content=m, mimetype="text/html")
    w_email.send()


def auction_fail(owner):
    o_email_address = [owner.email]

    o_email = EmailMessage()

    o_email.subject = 'К сожалению, ваш аукцион не состоялся!'

    o_email.from_email = "E-Auction.kg <eauction.kg@gmail.com>"
    o_email.to = o_email_address
    o_email.attach(content='owner', mimetype="text/html")
    o_email.send()
