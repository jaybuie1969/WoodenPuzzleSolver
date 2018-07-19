# WoodenPuzzleSolver
Python-based algorithm to find solution for the wooden puzzle in the pictures

Since every test project nowadays is apparently supposed to be up on a GitHub repository for all the world to see, instead of just figuring it out and going to the next thing, I'm uploading this here.

The puzzle shown in the pictures consists of a square holder and six pices, each one unit by three units.  Each side of a piece is divided into thirds, and each third is either flat, a hole, or has a knob.  Knobs fit into holes and flats fit smoothly together.  The bottom and lid of the holder have holes to hold any knobs they need to hold.

The goal is to put all six pieces fit smoothly together so that they all lay flat, with no wobbling.  Only then can the lid be put on.

This program uses a brute-force algorithm that recursively goes through all possible permutations of piece selection and organization (i.e. the piece is positioned right-side-up or upside-down, or rotated 180 degrees) until the solution is found.
