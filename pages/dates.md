---
title: "Dates and program"
---
# Program at a glance
<style>
#program, #program th, #program td {
    border: 1px solid gray;
    font-size: 85%;
    border-collapse: separate;
    border-spacing: 1px;
    color: #222222;
}
@media (min-width: 1200px) {	
    #program {
        margin-left: -50px;
        margin-right: -50px;
    }
}
#program th, #program td {
  padding: 5px;
  text-align: left;
}
#program div, #program a {
    color: white;
}
#program a:hover {
    text-decoration: underline;
}
#r00{
      background-color: #96B6BD;
 /*   appearance: none;*/
    box-shadow: 0 0 0px 8px gold;

  clip-path: polygon(-20% 0%, 100% 0%, 100% 100%, -20% 100%); /*left*/

}
#r00t{
      background-color: #96B6BD;
        box-shadow: 0 0 0px 8px gold;
        clip-path: polygon(-20% -20%, 100% -20%, 100% 100%, -20% 100%); /*top-left*/
    }


#t01b {
  background-color: #BDC0BF;
    box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
  font-weight: 350
}

#t01t {
  background-color: #BDC0BF;
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
  font-weight: 350
}
#r00b{
      background-color: #96B6BD;
        box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(-20% 0%, 100% 0%, 100% 120%, -20% 120%); /*bottom--*/
    }

#r01 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #BDC0BF;
  font-weight: 350

}

#r05 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #C4DFB3;
}

#r06 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #F9D368;
}

#r02 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #D9A9BC;
}
#r03 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #CDDFF0;
}
#t00 {
  background-color: #FFFFFF;
  text-align: center
  }
#t01 {
  background-color: #FFFFFF;
  font-weight: 350
}
#clr01 {
  background-color: #E5CFAE; 
}
#clr02 {
  background-color: #41CC1C 
}
#clr03 {
  background-color: #F1FF03
}
#clr04 {
  background-color: #FF7D03
}
#clr05 {
  background-color: #034DFF 
}
#clr06 {
  background-color: #FE03FF 
}
#t01s {
  background-color: #FFFFFF;
}

#cshort_v {
  background-color: #B9A3BE;
}
#clong_v {
  background-color: #B8CEDB;
}

#cmentor {
  background-color: #E8B8A2;
}
#cspecial {
  background-color: #74A1A7;
}
    #cspecial_t{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      border: 1px;}
     #cspecial_tr{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 120% -20%, 120% 100%, 0% 100%); /*top-right*/
      border: 1px;}
    #cspecial_br{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
      border: 1px;}

    #cspecial_b{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      border: 1px;}

    #title_legend{font-weight:300; font-size: 100%; text-align:left; color:white; padding-left: 6px; padding-right: 6px; white-space: nowrap; }
    #text_legend{font-weight:150; font-size: 80%; text-align:left; padding-left: 6px; }
    #cbreak_r{   background-color: #AEAEAE; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cbreak{   background-color: #AEAEAE; }
    #cbreak div, #cbreak_r div { color: #222222; }

    #clong_tr{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 120% -20%, 120% 100%, 0% 100%); /*top-right*/
      border: 1px;}

    #clong_t{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      border: 1px;}

    #clong_r{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #clong{   background-color: #0083AC;}

    #ckeynote_r{   background-color: #016297; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #ckeynote{   background-color: #016297;}

    #cshort_r{   background-color: #82538B; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cshort{   background-color: #82538B;}

    #cposter_r{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cposter_br{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
      border: 1px;}

    #cposter_b{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      border: 1px;}

    #cposter{   background-color: #248F85;}

td { 
    border: solid;
    border-width: 1px 0;
}
td:first-child {
  border-top: none;
}
td:last-child {
  border-bottom: none;
}
</style>
<script>
jQuery(document).ready(function($) {
    $('input[type= checkbox ]').click(function() {
        let index = $(this).attr('name').substr(3);
        index--;
        $('table tr').each(function() {
            $('td:eq(' + index + ')',this).toggle();
        });
        $('th.' + $(this).attr('name')).toggle();
    });
});
</script>

<table id="program" cellspacing="0" border="-1">
     <colgroup width="66"></colgroup>
     <colgroup width="65"></colgroup>
     <colgroup width="81"></colgroup>
     <colgroup span="5" width="138"></colgroup>
	 <tr>
		<td id='t01' class='col1' colspan=1 rowspan=1 height="62" width="280" ></td>
        <td id='t00' class='col2' style="text-align: center" align="center" width="300" rowspan=1 colspan=2 valign=center >Sunday<br>9-Jul</td>
        <td id='t00' class='col3' style="text-align: center" align="center" width="300" rowspan=1 colspan=2 valign=center >Monday<br>10-Jul</td>
        <td id='t00' class='col4' style="text-align: center" align="center" width="300" rowspan=1 colspan=2 valign=center >Tuesday<br>11-Jul</td>
        <td id='t00' class='col5' style="text-align: center" align="center" width="300" rowspan=1 colspan=3 valign=center >Wednesday<br>12-Jul</td>
        <td id='t00' class='col6' style="text-align: center" align="center" width="300" rowspan=1 colspan=1 valign=center >Thursday<br>13-Jul</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>7:00 - 7:30</td>
        <td id='t01s' class='col2' style="writing-mode: vertical-lr; text-align: center" align="center" valign=middle colspan=1 rowspan=21 width="150"><a href='doctoral.html'>Doctoral Symposium</a></td>
        <td id='t01' class='col2' rowspan=3></td>
        <td id='clr01' class='col3' style="text-align: center" align="center" valign=center colspan=1 rowspan=4>Check-in at Student Life Center Lobby</td>
        <td id='clr02' class='col3' style="text-align: center" align="center" valign=center colspan=1 rowspan=2>Breakfast at Rand</td>
        <td id='t01' class='col4' rowspan=2></td>
        <td id='clr02' class='col4' style="text-align: center" align="center" valign=center colspan=1 rowspan=2>Breakfast at Rand</td> 
        <td id='t01' class='col5' rowspan=2 colspan=2></td>
        <td id='clr02' class='col5' style="text-align: center" align="center" valign=center colspan=1 rowspan=2>Breakfast at Rand</td> 
        <td id='t01' class='col6' rowspan=4></td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>7:30 - 8:00</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>8:00 - 8:30</td>
        <td id='clr01' class='col3' style="text-align: center" align="center" valign=center colspan=1 rowspan=2>Poster setup time</td>
        <td id='clr01' class='col4' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center>Check-in at Student Life Center Lobby</td>
        <td id='clr01' class='col5' rowspan=2 colspan=1 style="text-align: center" align="center" valign=center>Check-in at Student Life Center Lobby</td>
        <td id='clr01' class='col5' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center>Gathertown virtual posters</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>8:30 - 9:00</td>
        <td id='clr01' class='col2' rowspan=1 style="text-align: center" align="center" valign=center>Check-in/coffee at Featheringill Atrium</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>9:00 - 9:30</td> 
        <td id='clr01' class='col2' rowspan=1 style="text-align: center" align="center" valign=center>Welcome at Featheringill Auditorium</td>
        <td id='clr01' class='col3' rowspan=1 colspan=2 style="text-align: center" align="center" valign=center>Welcome at Student Life Center Ballroom B/C</td>
        <td id='clr03' class='col4' rowspan=3 colspan=2 style="text-align:center" align="center" valign=center><a href='program.html' style='color:black'>Neuroimaging (5 orals, session ends at 10:15) at Student Life Center Ballroom B/C</td>
        <td id='clr03' class='col5' rowspan=2 colspan=3 style="text-align:center" align="center" valign=center><a href='program.html' style='color:black'>Segmentation 2 (3 orals, session starts at 9:15) at Student Life Center Ballroom B/C</td>
        <td id='t01' class='col6' rowspan=9 colspan=1 style="writing-mode: vertical-lr; text-align: center" align="center" valign=center colspan=1><a href="workshop_agenda.html">NVIDIA Workshop at Featheringill Atrium</a></td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>9:30 - 10:00</td>
        <td id='clr04' class='col2' rowspan=2 style="text-align: center" align="center" valign=center>Workshop at Featheringill Auditorium</td>
        <td id='clr03' class='col2' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center><a href='program.html' style='color:black'>Segmentation 1 (4 orals) at Student Life Center Ballroom B/C</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>10:00 - 10:30</td>
        <td id='clr05' class='col5' rowspan=3 colspan=3 style="text-align: center; color: white" align="center" valign=center>Coffee & Posters<br><br>Student Life Center Ballroom A and Board of Trust Meeting Room</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>10:30 - 11:00</td> 
        <td id='clr01' class='col2' rowspan=1 style="text-align: center" align="center" valign=center>Coffee at Featheringill Atrium</td>
        <td id='clr01' class='col3' rowspan=1 colspan=2 style="text-align: center" align="center" valign=center>MIDL</td>
        <td id='clr05' class='col4' rowspan=3 colspan=2 style="text-align: center; color: white" align="center" valign=center>Coffee & Posters<br><br>Student Life Center Ballroom A and Board of Trust Meeting Room</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>11:00 - 11:30</td>
        <td id='clr06' class='col2' rowspan=2 style="text-align: center" align="center" valign=center>Keynote: Dr. Lombaert at Featheringill Auditorium</td>
        <td id='clr05' class='col3' rowspan=2 colspan=2 style="text-align: center; color: white" align="center" valign=center>Coffee & Posters<br><br>Student Life Center Ballroom A and Board of Trust Meeting Room</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>11:30 - 12:00</td>
        <td id='clr02' class='col5' rowspan=2 colspan=3 style="text-align: center" align="center" valign=center>Lunch at Rand</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>12:00 - 12:30</td>
        <td id='clr04' class='col2' rowspan=2 style="text-align: center" align="center" valign=center>Career Panel at Featheringill Auditorium</td>
        <td id='clr02' class='col3' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center>Lunch at Rand</td>
        <td id='clr02' class='col4' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center>Lunch at Rand</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>12:30 - 13:00</td>
        <td id='clr06' class='col5' rowspan=2 colspan=3 style="text-align: center" align="center" valign=center><a href='keynotes.html' style='color:white'>Keynote Dr. Webster & Dr. Herrell<br><br>Student Life Center Ballroom B/C</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>13:00 - 13:30</td> 
        <td id='clr02' class='col2' rowspan=2 style="text-align: center" align="center" valign=center>Lunch at Featheringill Atrium</td>
        <td id='clr06' class='col3' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center><a href='keynotes.html' style='color:white'>Keynote: Dr. Rohde<br><br>Student Life Center Ballroom B/C</td>
        <td id='clr06' class='col4' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center><a href='keynotes.html' style='color:white'>Keynote: Dr. Yesha<br><br>Student Life Center Ballroom B/C</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>13:30 - 14:00</td>
        <td id='clr03' class='col5' rowspan=2 colspan=3 style="text-align: center" align="center" valign=center><a href='program.html' style='color:black'>Computer-assisted diagnosis (4 orals) at Student Life Center Ballroom B/C</td>
        <td id='t01' class='col6' rowspan=8></td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>14:00 - 14:30</td>
        <td id='clr06' class='col2' rowspan=6 style="text-align: center" align="center" valign=center>Grand Ole Opry/Opryland<br><br>Transportation to Grand Ole Opry: Meet by 24th Street Entrance to Featheringill Hill</td>
        <td id='clr03' class='col3' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center><a href='program.html' style='color:black'>Unsupervised/weakly supervised methods (4 orals) at Student Life Center Ballroom B/C</td>
        <td id='clr03' class='col4' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center><a href='program.html' style='color:black'>Semi-supervised/self-supervised methods (4 orals) at Student Life Center Ballroom B/C</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>14:30 - 15:00</td>
        <td id='clr05' class='col5' rowspan=2 colspan=3 style="text-align: center; color: white" align="center" valign=center>Coffee & Posters<br><br>Student Life Center Ballroom A and Board of Trust Meeting Room</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>15:00 - 15:30</td>
        <td id='clr05' class='col3' rowspan=2 colspan=2 style="text-align: center; color: white" align="center" valign=center>Coffee & Posters<br><br>Student Life Center Ballroom A and Board of Trust Meeting Room</td>
        <td id='clr05' class='col4' rowspan=2 colspan=2 style="text-align: center; color: white" align="center" valign=center>Coffee & Posters<br><br>Student Life Center Ballroom A and Board of Trust Meeting Room</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>15:30 - 16:00</td> 
        <td id='clr01' class='col5' rowspan=1 colspan=3 style="text-align: center" align="center" valign=center>Awards & closing<br><br>Student Life Center Ballroom B/C</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>16:00 - 16:30</td>
        <td id='clr03' class='col3' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center><a href='program.html' style='color:black'>Graph-based methods (3 orals, session ends at 4:45 PM) at Student Life Center Ballroom B/C</td>
        <td id='clr03' class='col4' rowspan=2 colspan=2 style="text-align: center" align="center" valign=center><a href='program.html' style='color:black'>Synthesis (4 orals) at Student Life Center Ballroom B/C</td>
        <td id='clr02' class='col5' rowspan=3 colspan=3 style="text-align: center" align="center" valign=center>Dinner at Rand until 7PM at Student Life Center Ballroom B/C</td>
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>16:30 - 17:00</td> 
     </tr>
     <tr>
        <td id='t01' class='col1' rowspan=1 height="20" style="text-align: center" valign=center>Evening</td>
        <td id='clr06' class='col2' rowspan=1 style="text-align: center" align="center" valign=center>Stillery dinner/drinks/music<br><br>Transportation to Stillery: Meet by 24th Street Entrance to Featheringill Hill</td>
        <td id='clr01' class='col3' rowspan=1 colspan=1 style="text-align: center" align="center" valign=center>Poster removal <strong>5-5:30PM</strong></td>
        <td id='clr06' class='col3' rowspan=1 colspan=1 style="text-align: center" align="center" valign=center>Buses at <strong>6PM</strong><br>Reception at NMAAM <strong>6:30-10PM</strong></td>
    <td id='clr06' class='col4' rowspan=1 colspan=2 style="text=align: center" align="center" valign=center>Walk to Parthenon at <strong>6-6:30PM</strong><br>Reception at <strong>6:30-7:30PM</strong><br>Dinner at <strong>7:30-8:30PM</strong><br>Music <strong>8:30-9:30PM</strong></td>
     </tr>
</table>

<br><a href="https://goo.gl/maps/RST8v5mrsRLp43vv7">Student Life Center: 310, 25th Avenue South, Nashville, TN 37240</a><br>

The buses that will go to the Reception at NMAAM will stop in front of the Student Life Center.<br>
<a href="https://goo.gl/maps/tiaWtWRMnmbs1fCx7">NMAMM: 510 Broadway, Nashville, TN 37203</a><br>

<a href="https://goo.gl/maps/K5P3wbDXpSRrATcD8">Parthenon: 2500 West End Ave, Nashville, TN 37203</a><br>

<a href="https://goo.gl/maps/BibtMigmEVRTxZTm9">Rand Dining Hall</a><br>

<a href="https://goo.gl/maps/kgsXjChubP9QYb7D6">Featheringill Hall</a><br>

Note that Nashville is on the [UTC-5 timezone](https://www.timeanddate.com/time/zone/usa/nashville).

# Important Dates
All deadlines are **23:59 [UTC-12](https://www.timeanddate.com/time/zones/aoe)/[Anywhere on Earth (AoE)](https://en.wikipedia.org/wiki/Anywhere_on_Earth)**.
## Full papers
[% .deadlines %]
* **<s>Paper registration deadline</s>** <s>8 January 2023</s>
* **<s>Paper submission deadline</s>** <s>15 January 2023</s>
* **<s>Reviews due</s>** <s>3 February 2023</s>
* **<s>Rebuttals</s>** <s>7&ndash;17 February 2023</s>
* **<s>Final decisions</s>** <s>24 February 2023</s> <s>2 March 2023</s>
* **<s>Camera ready</s>** 30 April 2023
[% / %]

## Short papers
[% .deadlines %]
* **<s>Paper submission deadline</s>** 7 April 2023
* **<s>Final decisions</s>** 28 April 2023
* **Camera ready (short papers)** Coming soon
[% / %]

## Conference dates
* **Main event**  10—12 July 2023
