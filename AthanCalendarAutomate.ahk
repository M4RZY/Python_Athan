^`::

loop 1000
{
sendinput {WheelDown 100}
sleep 1000
sendinput {Click 1060, 1120}
sleep 1000
sendinput {Enter}
sleep 1000
sendinput {WheelUp 100}
sleep 1000
sendinput {Click 1080, 780}
}
return

Escape::ExitApp