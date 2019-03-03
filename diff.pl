#!/usr/bin/perl
use strict; 
use warnings;


my $diffs = system("diff diagnosibility.pl product.pl");

print $diffs;
