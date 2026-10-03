<center><h1><b>Welcome to my personal athan project</b></h1></center>

<center><b>[Context]</b></center>

<paragraph></paragraph>

This project was one I had been meaning to do for a while as I couldn't find accurate athan software that linked up to my local mosque times, 

as well as this having an athan playing on my phone or on my laptop while I'm in college wouldn't have been ideal,

so I decided that I would give a new lease of life to two old laptops I had laying around and installed mx linux on them,

one of them will be a designated athan for my room so I can rush to prayer more hastily and have peace of mind knowing that I won't be to engrossed in my work that I end up forgetting a prayer or missing one. 



<center>as for the other laptop, I'm not sure what I'll do with it yet.</center>



<b>[V1]</b>

Here I'll go through each file and what I did so you can hopefully be able to do it aswell.

<paragraph></paragraph>
<paragraph></paragraph>

<center><b>The Folders:</b></center>

The `Calendars` folder contains all the pdf files of the calendar times, these times were downloaded from my local mosques website,

I used an autohotkey script to download each one.

```Format: yy:mm.pdf```

`Calendars - Copy` is just a copy of the original download as I thought I would mess up the renaming process.

(_I would recommend also doing the same_)



`Text_Files` is the result of converting the pdf files to text files and putting it in the format: 

```day, date, fajr, sunrise, dhuhr, asr, maghrib, isha```



and `Text_Files - Copy` is just a copy of the unchanged text files in case I messed up.

<paragraph></paragraph>
<paragraph></paragraph>

<center><b>The Sound Files:</b></center>

The .wma sound files come from the software "Athan" by Islamic Finder,
I changed them to .mp3 files so it would be compatible with the pygame library,
this athan can be found on YouTube by this [link](https://youtu.be/MaEzj5eRmjc?si=FZxwOf31b4SM8AG7)

<paragraph></paragraph>
<paragraph></paragraph>

<b><center>Python Files and AHK Script:</b></center>

`Athan.py` is the main python file, the others are what I used for formatting.

To give a brief description, it's a clock that runs but it checks every second if the time now is equal to any of the salah times for that day.

_Change the athan and dua lengths to the length of your athan file in seconds._

`Parse.py` was me trying to understand how to use the data from the files,

`TimetoTime.py` was an attempt to format the text files more to put them in the format `HH:MM:SS` instead of `HH:MM`.

`FormattingTextFiles.py`, `PDFRename.py` and `PDFTOTXT.py` are kinda self explanatory.

<center>AthanCalendarAutomate.ahk loop explanation:</center>

```
1. Scroll all the way down 
2. Click Download button
3. Press Enter
4. Scroll all the way up
5. Press right arrow (move to next month)
```
<paragraph></paragraph>
<paragraph></paragraph>

<b>[V2]</b> <b>Upgrades:</b>

- Added Witr alarm 15 mins before Fajr

- `Makkah.mp3` is now [`Athan.mp3`](https://youtu.be/MaEzj5eRmjc?si=cvNEEJ0JpKNIXoqU) which is the one on YouTube mentioned earlier

- Made code a bit neater in `Athan.py`
- Added testing comment in `prayer_time()` function




