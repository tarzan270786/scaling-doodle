#!/usr/bin/perl

use strict; 
use warnings; 
use IO::Socket; 
my $socket = new IO::Socket::INET ( 
	PeerAddr => 'localhost', 
	PeerPort => '45655', 
	Proto => 'tcp', 
); 
die "Could not create socket: $!n" unless $socket; 
print $socket "Hello this is socket connection!\n"; 
close($socket);
