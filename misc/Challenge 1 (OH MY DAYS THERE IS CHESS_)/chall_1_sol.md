# Challenge 1 (OH MY DAYS THERE IS CHESS_) solution

unfortunately, this was one of the harder challenges for me to solve. i spent much longer figuring this out as compared to the other misc challenge. at first, when i read the FEN, i thought it had something to do with decoding it, so i ran it through dcoder and tried to see if i'd get anything. i did not, as the FEN was slightly strange, and couldn't be decoded. i tried on many different websites to try to view it but it didn't work.

i then thought of the positions of the pieces, like 'a3', 'b4', etc, so i tried to convert it to the positions using `python-chess`. i thought it would give me some hexadecimal values that i could decode. it ultimately did not work either, as there were letters after f like g, which were not considered hexadecimal values. 

ah, now what? i've hit a roadblock. well, that is until i re-read the question. "I've been learning a bit more chess recently, but I'm having trouble understanding the point of this. Can you help me?" this might be a little bit of a stretch, but since chess positions and moves did not work, could it be how many points each piece was worth? 

i googled and i realised that for both black and white pieces, the pawn was worth 1 point, bishop and knights worth 3 points each, rook worth 5 points, queen worth 9 points. there was no king in the `FEN.txt` file. so i then decided to code a function which would total up each line's total, then i would try to decode it from there. 

and voila, it worked, giving me the flag: `bcactf{b15h0ps_4r3n7_kn16ht5_34j21nd92}`!