#!/bin/bash
set -e
build/vocab_count -min-count 1 -verbose 2 < textTCM > vocabTCM.txt
build/cooccur -memory 4.0 -vocab-file vocabTCM.txt -verbose 2 -window-size 50 < textTCM > cooccurrenceTCM.bin
build/shuffle -memory 4.0 -verbose 2 < cooccurrenceTCM.bin > cooccurrenceTCM.shuf.bin
build/glove -save-file vectorsTCM -threads 8 -input-file cooccurrenceTCM.shuf.bin -x-max 10 -iter 15 -vector-size 10 -binary 2 -vocab-file vocabTCM.txt -verbose 2
