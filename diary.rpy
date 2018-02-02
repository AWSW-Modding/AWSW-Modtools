label mod_remy_christmas_read_diary:

# F:\PlayMusic\Crinkles\Crinkles - Soundtrack from a Box 4\Crinkles - Soundtrack from a Box 4 - 08 Imperial.flac
# F:\PlayMusic\Crinkles\Crinkles - Soundtrack from a Box 13\Crinkles - Soundtrack from a Box 13 - 14 Drowning.flac
# F:\PlayMusic\Crinkles\Crinkles - Soundtrack From A Box 7\Crinkles - Soundtrack From A Box 7 - 10 Black Rose.flac
# F:\PlayMusic\Crinkles\Crinkles - Soundtrack from a Box 4\Crinkles - Soundtrack from a Box 4 - 10 The Hunt.flac

play music "mx/down_the_well.ogg" fadein 2.0

m "Looking again, the diary is even more unused than I thought originally - it seems to be barely half filled."
m "The name on the front is 'Amelia' in cursive handwriting and faded blue ink."
m "Opening it, the pages feel delicate to the touch."

show remy_christmas diary with fade
$ renpy.pause(1.0)

play sound "fx/envelope.wav"
nvl clear

window show

n "Today I got a diary to note things in. I guess I should start off gently, talking about myself."
n "Some would call me an inventor. I don't really agree with that. I'm just good at taking ideas and bringing them into our world."
n "Our current project is to streamline the entire hospital process for our kind. The current tools and equipment available for use are almost completely incapable of accomodating us, as if designed for another species entirely."
n "This can be seen in almost every aspect of our lives - our tables, chairs and even toilets."
n "Some would say they were designed for humans. Our ancestors were obsessed with them, some of us still are. It saddens me that these views are still prevalent, especially in the positions that matter most: our government and academics."
n "I'm lucky to be a group of scientists where these views are considered antiquated by all and actively moving forwards."

nvl clear
play sound "fx/envelope.wav"

n "Day two"
n "So I got this diary yesterday. It's growing on me already. Or not. It's weird to write stuff in there. I'm really not sure why I got it at all. Impulse I guess."
n "Anyway, there was talk at work about a new politician. The usual discussions - how they were going to ruin the economy, education, all of it. Someone said they'd heard that the person in question had just bought the position. I wouldn't put it past politicians. Rotten to the core, the lot of them."
n "Her name was Emera. I'd say even the name sounds bad but I'd not stoop that low, except for maybe here. Her policies were interestingly similar to the status quo. I guess I'll have to see if there's a proper correlation."

nvl clear
play sound "fx/envelope.wav"

n "Day three"
n "Today's my official day off work. I call it one of my unpaid work days, as in reality I just spend my time jotting notes and calculations. Not that I mind at all, if I didn't want to do it, I wouldn't."
n "In two days, our project will be going to an expert panel to decide if we're going to get further governmental funding. As much as we all dislike it, we've got to go for it; there's little to no funding out there otherwise."
n "I detest how little our species seems to care about our own technological advancement with only a few individuals willing and able to contribute to making everyone's lives easier."

nvl clear
play sound "fx/envelope.wav"

n "Day four"
n "At my second day off, I'm bored stiff. I'm at a mental block with work and need to discuss it properly with someone to work out the finer details."
n "I hope we'll have it all completely ready by the time we enter the office where we'll be getting judged by the fact checking committee, if not, then it's back to the drawing board for several months whilst we go over their feedback and cover the holes."
n "At least we have a fair chance with them. They seem to do a pretty good job at knowing when a project is fleshed out enough to work out - almost everything that gets funded goes to completion without too much hassle and bad turns."
n "They give decent feedback as well, especially with what's not quite thought out as well as it could be."
n "Even though they're called the fact checking committee, our team at least hasn't had to worry about getting the facts wrong, at least for a very long time."

nvl clear
play sound "fx/envelope.wav"

n "Day five"
n "I'm writing this before I leave. It's making me kind of nervous actually, even though it probably shouldn't."
n "Ten minutes before I should be going... It'll all be fine."

show whiteroom gray with dissolve
hide remy_christmas diary
window hide

show remy normal b gray at right with easeinright

Ry "Hello, you're Amelia, aren't you? Representing the project on redesigning equipment used for hospitals?"
Amelia "Yes and yes."
Ry "Would you like to explain your project?"

Amelia "Well, we start off with the context: the equipment we use is badly designed for our kind."
Amelia "Especially so in hospitals - where every mistake can be fatal."
Amelia "Redesigning even the beds so they can be used on a subject lying face up would be a significant improvement."
Amelia "In their current state, only furred dragons, runners and certain flyers can really use them. Earth dragons simply can't or their spikes will embed in the mattress."
Amelia "Even in those that can physically use them, many report pain if they repeatedly do so, presumably due to the lack of tailorship in design to their subspecies."
Amelia "Our project aims to help by recreating equipment fit for purpose."
Amelia "We need funding for our project so we can afford both to build prototypes as well as the final designs."
Amelia "We also need to educate doctors and practitioners on how to use the products once the design is finalised."
Amelia "Having people die due to untrained professionals is unacceptable so we'd need additional funding to help fight against that."
Amelia "We propose to completely redesign medical equipment, beyond the simple such that they can be effectively used."
Amelia "Our technological advancements will help to make this a reality. Just recently, a method for injecting directly into the bloodstream was discovered without damaging our outer scales."
Amelia "Making this sort of thing available to the sector in general cheaply will vastly increase the survival rate."
Amelia "Damaged scales can and do easily cave in on themselves, causing massive bleeding if they hit arteries."
Amelia "Preventing this will significantly increase the lifespan of those who require minimal amounts of surgery."
Amelia "I think that's all for now"

$ renpy.pause(1.0)
play sound "fx/scribblex.ogg"
$ renpy.pause(1.0)

Ry "I think I've got that all written down."
Ry smile b gray "Just between us, I think the idea really stands out, though we have to stay completely neutral and discuss it with everyone else on the panel."
Amelia "Are there any forms I have to sign or is that it for now?"
Ry "You can go now, we'll decide if your project has approval fairly soon. Thank you for applying and helping to make our world a better place for everyone."

scene black with dissolvemed
$ renpy.pause (0.5)
show remy_christmas diary with fade
$ renpy.pause (1.0)

window show

n ""
n "I think the meeting went ok. I just felt a little robotic with all my points, though hopefully that won't matter in the end. Now that work's over, I think I need a rest."

nvl clear
play sound "fx/envelope.wav"

n "I can't really remember what day it's been since I bought this diary. I haven't really written in it for a while. I've been too busy stressing about work to really write things down in here."
n "We got the results back from the committee today. We didn't get the grant after all. They didn't think there was enough money to cover what we proposed, which is fair to an extent. It annoys me that they didn't propose cutting parts of it but I guess that's how it goes in politics."
n "We discussed it and decided that to move forwards, we'd have to tighten our scope. We can probably get the next grant for the less taxing things like just reshaping equipment to be ergonomic."
n "Even though it's less interesting for me as an individual, it will still be useful for society as a whole. I can develop the better injection technology in my own time. I have access to the equipment I'd need from work anyway."

nvl clear
play sound "fx/envelope.wav"

n "Another day off work. I decided to go to the café to do some theory work on my side project. The white noise makes it easier for me to work and the server likes me, so I sometimes get free food on them, which is nice."

show cafe gray with dissolve
hide remy_christmas diary
window hide

Amelia "(So now I'm here at the cafe, I should probably take a seat and order a meal)"

play sound "fx/chair.wav"
$ renpy.pause(2.0)

show adine normal b gray flip at left with easeinleft

Ad "Oh, hello Amelia. Nice to see you again."
Amelia "Nice to see you as well Adine, how have you been doing?"
Ad think b gray flip "The usual I guess. I've just started to volunteer over at the hatchery. It's nice to know I'm doing something useful with my life"
Ad "Do you want anything, or just here to relax again?"
Amelia "I'll just have a coffee, and a strong one. I'm here for work again and I need it to concentrate properly on what I'm doing."
Ad giggle b gray flip "Sure, let me just go and fetch it for you"

hide adine with easeoutright

Amelia "(I guess I should start doing stuff now. Starting with getting out my bag)"

play sound "fx/unwrap.ogg"
Amelia "(Well, time to get to it)"
play sound "fx/writing.ogg"

$ renpy.pause(1.0)
show remy normal b gray at right with easeinright

Ry "You mind if I sit next to you?"
Amelia "Not at all. Do I know you at all?"
Ry "You do look familiar now I think about it. Are you by chance someone who I've met at the committee?"
Amelia "Yes, that would be it. Funnily enough I'm here to do some work on a small side project of mine on helping hospital patients survive injections."
Ry "I think I remember that now. What you said was rather impressive if it could have been made to work properly within the budget. Though as you know, the committee weren't convinced it could have been."
Amelia "I get that now. That wasn't an aspect we considered really, it seems rather silly now that we completely overlooked it."
Ry "I guess it might have been. That's something you'll definitely want to look over if and when your team resubmits it."

$ renpy.pause (2.0)

show adine normal b gray flip at left with easeinleft

Ad "One coffee for Amelia."
Ad "Would the other gentleman like to order anything?"
Ry shy b gray "Er - A tea would be nice to have."
Ad "And one tea for you."

show adine normal b gray
hide adine with easeoutleft
play sound "fx/coffee.wav"

Amelia "So, what sorts of things do you do in your spare time?"
Ry "Well, sometimes I play computer games and love books. I don't really like saying what I do in case I embarrass myself."
Amelia "Huh. Well, I think you'd find it hard to say something that would make me disappointed in you or something like that."
Ry "If you say so."
Amelia "I mean, what you do at work is fantastic, the committee's never been better in terms of being unbiased and practically useful, even if our project was deemed as unfeasible."
Ry normal b gray "Well, I am rather proud of what we've managed to achieve with it in such a short time. Our reputation as an unbiased source is much better than it's ever been. Not only that, we're also more efficient at going through projects than before."
Ry "I also consider the work we do very important to the survival and prosperity of our species as a whole."
Amelia "I very much agree with you there - without the committee, we would be stuck in an age where nobody knew what was going on, constantly going over budget and allowing projects that are completely unethical to perform."

show adine normal b gray flip at left with easeinleft

Ad "And a tea for the gentleman."
Ry "Thank you very much."
Ad "Oh, am I in the way of an important discussion?"
Ry shy b gray "Not at all."
Ry "In any case, I should be going. It was nice talking to you and thanks again for the tea."
Amelia "In case you want to call, here's my number."

play sound "fx/scribblex.ogg"
$ renpy.pause(1.0)

Ry "And er, you can take mine in case you want to call me."
Amelia "I'll be sure to."

hide remy with easeoutright
hide adine with easeoutleft

scene black with dissolvemed
$ renpy.pause (0.5)
show remy_christmas diary with fade
$ renpy.pause (1.0)

window show

n "It turned out much better than I expected, I ran into the dragon who I suggested the project to. We chatted about work, had something to drink and exchanged numbers. He seems a very interesting person."
n "Maybe we'll end up talking again. I quite liked our conversation and he had lots of things to talk about."

nvl clear
play sound "fx/envelope.wav"

n "I don't think I'm going to bother writing stuff about the date since I got this anymore. It seems rather superfluous, especially given I've forgotten when I got it"
n "Today at work we did some more work on making sure that what we would be proposing would be specific and cost effective, using the feedback we got from the committee to help us reign in our scope to what would be feasible with the money available."

play sound "fx/phonering.ogg"
hide remy_christmas diary
window hide
$ renpy.pause (1.0)
play sound "fx/phonepickup.ogg"
$ renpy.pause (1.0)

Amelia "Hello?"
Ry "Hi, it's Remy, we met at the café a couple of days ago and I thought it would be a good idea to have a proper meal together formally. I'm sorry about what happened a couple of days ago, I guess I just got nervous about it all."
Amelia "Sure. A meal together would be nice. Where and when?"
Ry "I was thinking about my home next week and making something especially - are you vegetarian?"
Amelia "That would be great and no, I'm not vegetarian."
Ry "See you then."

show remy_christmas diary with fade
$ renpy.pause (1.0)
window show

n "Remy called and invited me to a formal meal at his house. I'm pretty sure this was his way of asking me out on a date. His intellect and wishes for knowledge are so relatable to myself it's uncanny."
n "I can relate to everything he says and does, I'm surprised a person so similar to me can even exist in this world. His nervousness is completely understandable in a world as harsh and unforgiving as our own"
n "I think I might be falling for him."

nvl clear
play sound "fx/envelope.wav"

n "Another day at work done. We're going to submit the revised project to the committee again very soon. I'm slightly worried about how this will effect my relationship with Remy, if we do get the grant, it could be seen as severe misjudgement and bias."
n "Next time we meet, probably the next time I'll write in this knowing me, I'll know what's happening for certain. I can only hope that he'll still want to be with me in the future."
n "He's the only one that matters to me right now, I'm not sure how this could have happened to me and I'm afraid to express to him how much he means to me."

nvl clear
play sound "fx/envelope.wav"

# Next meeting with Remy, discuss their relationship as well as needing to stay impartial

n "We met again today and agreed it would be best not to see each other again, at least until we know if our team's won the grant."
n "For some reason, I feel like I want it less and less. I don't think there's ever been a time where a person's come before my job before, but I think this might be the first time."
n "I wouldn't sabotage the project, but at the same time, I don't see myself being able to talk to Remy if we do get the grant - both our jobs would be at stake. I can't imagine being without him now, even though it's only been about a month since we met."
n "I guess this might be what love feels like. It's a weird feeling and I'm not sure if I like it. Being torn apart from him sounds like it would be the worst feeling imaginable and I'm not sure if I could cope with it."

# As Christmas is coming up, she goes shopping and gets a tie that can remind him of her.

nvl clear
play sound "fx/envelope.wav"

n "I've only just noticed that it's Christmas soon. As I might only be seeing him once more for a while, I should get something for him to remind me of him."

window hide
$ renpy.pause(1)
show remy_christmas tie with dissolvemed
$ renpy.pause(3.14)
hide remy_christmas tie with dissolvemed
$ renpy.pause(1)
show remy_christmas diary with fade
window show

n "I ended up getting him a red tie. I think it would look good with the collar he's got already."
n "I hope he'll like it when I give it to him once they've decided who should get the grant."
n "If we don't get it, I guess it'll just be a race against time until we do, so it's really just a waiting game at this point. I do want to be able to spend this Christmas with him though."

nvl clear
play sound "fx/envelope.wav"
$ renpy.pause (1.0)
play sound "fx/phonering.ogg"
hide remy_christmas diary
window hide
$ renpy.pause (1.0)
play sound "fx/phonepickup.ogg"
$ renpy.pause (1.0)

Amelia "Hello?"
Ry "Hey Amelia, it's Remy."
Amelia "Hey Remy, how are you doing?"
Ry "Great actually, I'm calling about some good news - the committee's decided to award your team the grant. Isn't this great? You'll be able to finally help those who need it the most"
Amelia "That's great, I'll make sure to forward the message to the rest of the team so we can start preparing for what we've got to do."
Amelia "There's one thing I'm worried about now though, and that's what will happen with us now we're properly together and how this'll affect our relationship."
Ry "Well, we were completely unbiased in our decision making, I wasn't even involved with your case because I knew that I'd say yes without hesitation."
Amelia "Do they know that now?"
Ry "No... Which means they'd probably think I'm lying to protect myself. Even though I'm not, it's a sensible thing to default to. I wouldn't blame them for it."
Ry "Now if it comes out, both our jobs could be in jeopardy, for abusing our positions and not making it officially clear we had a conflict in interests."
Amelia "What do you suggest we do about it? "
Ry "Well there's only one thing we really can do about it"
Amelia "I guess... I'll really miss you Remy. I don't know how it's happened that I've fallen for you so much in the short time we've had together."
Ry "Me neither."
$ renpy.pause (1.0)
Ry "It's hard to talk about this sort of stuff. I don't really know how I feel, just that you mean much more to me than you really should."
Amelia "It's ok. I know the feeling and I get that as well sometimes. It's not fun, though it's a part of life and getting older."
Ry "Well, what do you suggest we do? We can't stay together with this happening, and I'm not going to be the one to make you lose your job."
Amelia "Why don't we have one more visit to discuss this? To put everything to rest at least while everything's going on."
Ry "Alright. My place tomorrow?"
Amelia "Sure."
Amelia "Love you~"
Ry "You too."

show remy_christmas diary with fade
$ renpy.pause (1.0)
window show

n "Remy called today about the grant. Apparently the committee decided that our project was good enough to continue forwards and receive the grant for."
n "Whilst this is great for my work prospects, it's not going to be great for our relationship. He suggested that we meet one more time to discuss it more, like we'd previously decided."
n "I guess this'll be a good a time as any to give him his present, even if it is a couple of weeks early. I guess it can't really be helped."
n "I'll really miss him"

nvl clear
play sound "fx/envelope.wav"

n "Today's the day we arranged to visit. I've wrapped his present and will give it to him as soon as we meet in his home."
n "I should be going now. I'm looking forwards to it and not at the same time. It seems like forever since I met him for the first time, even though it was really recent."

show remyapt gray with dissolve
hide remy_christmas diary
window hide
play sound "fx/knocking2.ogg"
$ renpy.pause(2.5)

Ry "Hello, is this Amelia?"
Amelia "It is, could I come in? It's really cold out here."
Ry "Of course, come in Amelia, I've made something especially for you."

show remy normal b gray at right with easeinright
play music "mx/black_rose.ogg" fadein 2.0

Amelia "I can tell, it smells delicious in here. What have you been cooking?"
Ry "Roast mouflon. Think Christmas come early for the both of us. I've got some gravy cooking as well which we can eat it with. It'll be ready to eat pretty soon."
Amelia "That's sounds mouthwatering. Very much looking forwards to having that."
Ry "I'm surprised you trust my cooking so much already, you've only had it once."
Amelia "Ah, but that was quite possibly the best meal I've ever had, so I know what to expect."
Ry shy b gray "Well let's hope it's as good as you're expecting."

play sound "fx/veggies.ogg"
$ renpy.pause(2.0)

Ry normal b gray "I think it's ready now, I'll just serve it. The table's already laid, feel free to sit down."
Amelia "Is there anything you need help with at all?"
Ry "No, I'm, fine. Just putting it on the plates now. Do you want to have anything to drink?"
Amelia "Water will be fine for me - and oh wow that's impressive. That looks fit for a king."
Ry smile b gray "I'm glad you like it, now let's see how it tastes shall we?"
Amelia "I'll just sit down now so I can admire it completely."

play sound "fx/chair.wav"
$ renpy.pause(2.0)

m "He put down the plate in front of me, on it was steaming hot mouflon, with a red sauce on top. It looked like he'd practiced this a lot, which I suppose was a good thing - striving for perfection in whatever he does."
m "I took a bite and was immediately greeted with the succulent juices of the meat as it split at the lightest touch of my maw, the sauce enhancing the taste massively, adding a spicy component."
Amelia "It tastes like perfection - just right for a Christmas meal."
Ry "I'm happy you like it"
m "We ate and ate, finishing the wonderful meal Remy had made and prepared for us, going on to a cake dessert."
Amelia "I'm stuffed, that meal was delicious. Definitely worthy of a prize of some form."
Ry look b gray "It wasn't that great..."
Amelia "It was. And I should get our your present I bought for you."
Ry "You bought me something? But I don't have anything to give back to you."
Amelia "Of course I did. And that meal was definitely enough of a gift for me, it was possibly the best thing I've ever had the pleasure of eating."
m "I brought out the box I folded the tie into and gave it to him, putting it directly into his paws."
Amelia "Why don't you open it now so I can know what you think of it?"
Ry "I guess I can do that. I normally wait for the day, but as we're not going to see each other for so long"

play sound "fx/unwrap.ogg"

Amelia "I thought it would recognise you of me, red like my scales. Why don't you try it on?"
Ry smile b gray "It's amazing, more than I could have asked for."

play sound "fx/undress.ogg"
$ renpy.pause(2)

Ry smile gray "How do I look?"
Amelia "Smart and handsome. As long as you wear it, you'll be with me, in a way."
Ry "I'll keep that in mind for the time we're apart. That you're still with me. Forever."
Amelia "I'm glad you will. Now, what are we going to do about all this? I don't think we should see each other, hence why this all happened now and not later on the day itself."
Ry sad gray "I guess we shouldn't. We should leave enough time for it not to look suspicious at least, do you think 6 months will do?"
Amelia "I'm not sure if I could last that long without you... You've somehow become my life and I don't think I could go back to just me by myself."
Ry "Me neither... But I'm not having you loosing your job over something that can be solved simply by waiting. It's the logical thing to do."
Amelia "It is. I'll just have to live with it."
Ry "I love you, Amelia."
Amelia "I love you too Remy."
Ry normal gray "Why don't you rest here for the night? It's cold outside."
Amelia "Sure. That sounds good to me."

hide remy with easeoutright
scene black with dissolvemed
$ renpy.pause(5)
show remy_christmas diary with fade
$ renpy.pause(1.0)
window show

n ""
n "I'm back now. It was... Definitely a night to remember. I'm not sure how he managed to get drunk on wine but he did. He loved his tie and it looks amazing on him. He said the cutest thing to me: 'I'll never go without this'"
n "And I believe him. It make him look so much better, more handsome. He even suggested that I move in after this is all over. I want that. I really really want that."

nvl clear
play sound "fx/envelope.wav"

n "I've been starting to feel ill now, I hope it'll be nothing. Though if it continues like this, I'll have to take a couple of days off work."
n "That will just mean I'll be working from home unless it gets really bad."
n "I think I'll try and have some rest now, possibly get some sleep."

nvl clear
play sound "fx/envelope.wav"

n "It's still bad, even getting worse I'd say. I'd probably take some pain killers if I had any."

$ renpy.pause(1.0)

n "I've just gone to the store to get some. It was really cold out there, maybe I shouldn't have gone out at night in the middle of winter."
n "At least I have a load of them now. I've got enough food to last me quite a while and those should certainly last me until I'm better."

nvl clear
play sound "fx/envelope.wav"

n "I think I've finally worked out the source of my illness."
n "All the signs point to pregnancy... It would make sense considering what happened that last day I saw Remy."
n "I hope he still loves me when we can finally speak again."
n "Well, I should be responsible and at least go to the store to make sure my theory's right. It's not like the testers are very expensive."

scene black with dissolvemed
hide remy_christmas diary
window hide
$ renpy.pause (1.0)


# End of diary.

if chapter4unplayed == False:
    c "(I guess I've learned some more about Amelia at least.)"
    jump chapter4chars

elif chapter3unplayed == False:
    c "(That was the last page with writing on it. I wonder what happened to her.)"
    jump chapter3chars
