#!/usr/local/bin/perl -w
use strict;


my @sentences = ($ARGV[0]);

# clear trailing punctuation


foreach (@sentences) {
    print yoda($_)."\n"
}

sub yoda {

    my ($sentence) = @_;

    my @pivot_words = qw/is be will show do try are teach have/;
    
    # Find out if I have a pivot word and grab the one with the lowest index
    my $pivot = (sort { $a->[1] <=> $b->[1]}
                 grep {$_->[1] > 0} 
                 map  { [" $_ ",index($sentence," $_ ")] } @pivot_words)[0];
                        #^^^^^^                 ^^^^^^^
                                                # Change to fix the problem [zdog]
                                                # pointed out - THX [zdog]

    # No pivot words

     # remove trailing punctuation

    $sentence =~ s/[[:punct:]]//;

    return $sentence if (!$pivot);

    # Pivot the sentence
    $sentence = substr($sentence,$pivot->[1]+length($pivot->[0]),length($sentence)).
                 ", ".
                substr($sentence,0,$pivot->[1]).
                $pivot->[0];
    
    # Clear leading spaces
    $sentence =~ s/^\s+//;

    $sentence =~ s/\s$//; 
    # Sentence case
    $sentence = ucfirst(lc($sentence));

    $sentence = $sentence . "."

}
