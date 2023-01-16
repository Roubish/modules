#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 08:08:00 2022

@author: dragon
"""

import pikepdf


pdf = pikepdf.open('/home/dragon/Downloads/Dhani Wallet - Transaction Statement Details - May 11 2022.pdf', password='RAPO8295',allow_overwriting_input=True)

print("\nProcessing...\n")


pdf.save('/home/dragon/Downloads/Dhani Wallet - Transaction Statement Details - May 11 2022.pdf')

print("The password successfully removed from the PDF")
