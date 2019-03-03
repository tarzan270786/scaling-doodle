#!/usr/bin/perl 
use strict ;
use warnings ;
my $total = 0 ;
&getnumbers; 
my $number = 0 ;
my @numbers;
foreach $number(@numbers) {
	print "$number\n" ;
	$total +=$number ; 
}

print ("The total is $total \n");
sub getnumbers {
	my $line = <STDIN>; 
	 $line =~ s/^\s+|\s*\n$//g; # remove all the leading and trailing space 
	 @numbers = split(/\s+/,$line);

}
