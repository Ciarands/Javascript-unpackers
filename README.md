# Javascript-unpackers
Simple scripts I have written for extracting from non-destructive JS packers

## Motivation
Reversing obfuscated JS on the web I often find packed Javascript, 99% of the time all you have to do is replace `eval` with `console.log`. However, I recently ran into a few samples which attempt to nest this packed code to slow down reverse engineers.
This is just a collection of scripts that I have written to recursively extract these packers so that we can analyse them properly, without having to spend 5 minutes manually doing it.

## Support
Join the [discord](https://discord.gg/z2r8e8neQ7) for support.
