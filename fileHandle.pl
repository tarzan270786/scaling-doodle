#!/usr/bin/perl

use strict ;
use warnings ;
my $line;
open(FHR, '<',"sanity_final_CVEKQV4FDWVG5WN_DWDB.log") or die "Some error $!\n";
#$line = <FHR>; 
while( $line =  <FHR>) {
print $line;
}
close(FHR);
