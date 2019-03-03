#!/usr/bin/perl
use strict ;
use warnings ;
my $count=0;
my $input=undef;
open(FHR ,"<sanity_final_CVEKQV4FDWVG5WN_DWDB.log") or die "cannot open the file $!" ;

while (<FHR>){
	$input = <FHR>;
	next  if $input =~ /^$/;
	#$count++;
	print $input;
}
close(FHR);
