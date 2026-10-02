# Arabic narration — candidates (Syrian dialect, like videos 1 and 2)

One entry per spoken line, in order: when it plays in the planned cut (estimated; there is no render yet), its key in
`config/narration.json`, the English line, then 2 Arabic versions. **★ = the one I recommend.** Write your pick after
**Decision:** (1, 2, ★, or your own wording; `remove` to cut a line). Then
`python3 scripts/build_narration_ar.py` turns the decisions into `config/narration_ar.json`, and the recorder
(`python3 scripts/record_server.py`, http://localhost:8765) shows every decided line ready to record. Undecided
lines show as pending and can't be recorded yet; you can also type a line on its card in the recorder, which makes it ready.

The scenes re-time themselves to your recorded voice, so an Arabic line can run longer or shorter than the English. Try to stay within about ±30%.

## How it's written

- **Dialect and spelling follow video 2's script** as you recorded it: spoken Syrian, written the way it's said
  (هيي، التشات، كتبا/منا without the final ه, هلّق، هيك، شي، كتير، متل، عم، رح، إنو، عالـ).
- **It's adapted, not translated.** Spoken Arabic gets whole sentences and video 2's connectors: طيب to turn to a
  new question, يعني to rephrase, لهيك for "that's why", باختصار for the recap.
- **Video 2's figures carry over:** الكاتب is the same writer; «الإيدين» is the new helper, the way الطابعة was;
  every bit ends on a question; the last line mirrors «يعني ما رسما… كتبا كتابة».
- **Quotes match the on-screen text exactly** (the request slip, the dial, the checklist, the timeline words),
  so the line you pick decides what I draw.

## Words used

| English | Arabic | note |
|---|---|---|
| AI agent | إيجنت / الـ AI Agent | alternative: وكيل ذكاء اصطناعي. The on-screen chip says «AI Agent» |
| the writer (the model) | الكاتب | video 2's word |
| the hands (the program) | الإيدين | the new helper; «برنامج صغير» when introduced |
| model | نموذج | as in video 2 |
| request | طلب | the slip the writer writes |
| lap / loop | لفّة | دورة once, in bit1.6 option 1; pick one |
| menu | قائمة | alternative: منيو |
| desk (context window) | الطاولة | the English term once on screen |
| slips | ورقات | |
| notebook / summary / to-do | دفتر / ملخّص / قائمة المهام | ليستة is also natural |
| discount | خصم | |
| the dial's needle | الإبرة | not المؤشر, which was the cursor in video 2 |
| shopkeeper | البيّاع | |
| boss (the CEO agent) | المدير | |
| eternal transcendence | التسامي الأبدي | |

## Check before recording

- **The company isn't named.** The lines say "an AI" and "the people who ran the test". If you want to name Anthropic, say where.
- **bit3_desk.9 (the FBI email) is optional.** Write `remove` under its Decision to cut it.
- **On-screen words follow your picks:** the request in bit1.2, the dial «لأ»/«أكيد» in bit 4, the three words in
  bit5.2, the checklist in bit6.3, and «التسامي الأبدي» in bit6.6 (or keep the English all-caps original there).
- **Length:** at video 2's pace this is about 5:50 with the end card. The hook (~43 s) is the longest part; hook.3 is the line to trim if it drags.

---

## Hook: a shop nobody ran by hand

### ~0:01.5 – 0:05.8  ·  `hook.1`  ·  EN ~4.3s, then 0.4s pause

EN: For a whole month, a small shop in an office was run by an AI.

★ 1) شهر كامل، في محل صغير بمكتب، ما كان يديرو حدا غير ذكاء اصطناعي.  
   2) لمدة شهر كامل، محل صغير جوا مكتب شركة كان عم يديرو ذكاء اصطناعي.  
   3) هالمحل الصغير، بقلب مكتب، أدارو ذكاء اصطناعي شهر كامل لحالو.  

> Option 1 echoes video 2's opening «ما حدا رسما…» with «ما كان يديرو حدا غير…».

**Decision:** 

### ~0:06.2 – 0:11.6  ·  `hook.2`  ·  EN ~5.4s, then 0.6s pause

EN: It picked what to sell, set the prices, ordered stock and answered every customer. People only carried the boxes.

★ 1) هوي اللي نقّى شو يبيع، وحط الأسعار، وطلب البضاعة، وردّ على كل زبون. والناس بس كانوا يشيلوا الكراتين.  
   2) هوي اختار البضاعة، وسعّرا، وطلبا من الموردين، وحكى مع الزباين. والناس شغلتن بس يحملوا الصناديق.  

**Decision:** 

### ~0:12.2 – 0:23.1  ·  `hook.3`  ·  EN ~10.9s, then 1.0s pause

EN: By the end of the month it was selling metal cubes below cost, giving a discount to anyone who asked, and telling the staff it would deliver orders in person, in a blue blazer and a red tie.

★ 1) وبآخر الشهر، كان عم يبيع مكعبات معدن بأقل من حقها، ويعطي خصم لكل مين طلب، وقال للموظفين إنو رح يوصّل الطلبات بنفسو… لابس جاكيت زرقا وكرافة حمرا.  
   2) ولما خلص الشهر؟ مكعبات معدن عم تنباع بخسارة، خصومات لأي حدا بيطلب، ووعد الموظفين إنو رح يجيب الطلبات بإيدو، بجاكيت زرقا وكرافة حمرا.  

> The report says a blue blazer, so زرقا, not كحلي. This is the longest line of the hook; if the hook feels slow, trim here first.

**Decision:** 

### ~0:24.1 – 0:34.7  ·  `hook.4`  ·  EN ~10.6s, then 0.6s pause

EN: But the AI behind it can't lift a box or press a button. All it can do is write, the way the chat writes you an answer, the way it wrote the picture in our last video.

★ 1) بس هالذكاء الاصطناعي ما بيقدر يشيل كرتونة ولا يكبس زر. كل اللي بيعرف يعملو إنو يكتب: متل ما التشات بيكتبلك جواب، ومتل ما كتب الصورة بالفيديو الماضي.  
   2) والغريب إنو ما بيقدر لا يشيل علبة ولا يكبس زر. هوي بس بيكتب، متل التشات لما بيكتبلك جواب، ومتل ما شفناه بيكتب الصورة بالفيديو اللي قبل.  

> This is where the title is paid (~0:25): it only writes.

**Decision:** 

### ~0:35.3 – 0:39.6  ·  `hook.5`  ·  EN ~4.3s, then 1.6s pause

EN: So how does writing run a shop? And why did this one go so wrong?

★ 1) طيب كيف الكتابة بتدير محل؟ وليش هالمحل بالذات خربت معو هالقد؟  
   2) فكيف شي ما بيعرف غير يكتب، أدار محل؟ وليش طلعت معو هيك؟  

**Decision:** 

## Bit 1: the writer and its hands

### ~0:42.7 – 0:47.6  ·  `bit1_loop.1`  ·  EN ~4.9s, then 0.6s pause

EN: Inside, it's the same writer: it reads everything in front of it and writes what comes next.

★ 1) من جوا، هوي نفس الكاتب: بيقرا كل شي قدامو، وبيكتب اللي بعدو.  
   2) جواتو في نفس الكاتب اللي شفناه: بيقرا كلشي مكتوب قدامو، وبيكتب الشي الجاي.  

> الكاتب is video 2's word for the model; keeping it ties the two videos together.

**Decision:** 

### ~0:48.2 – 0:51.6  ·  `bit1_loop.2`  ·  EN ~3.4s, then 0.8s pause

EN: So it writes a request: "Email the supplier: forty cans of soda."

★ 1) فبيكتب طلب: «ابعت إيميل للمورّد: أربعين علبة كولا.»  
   2) فبيكتب سطر: «إيميل للمورّد: بدنا أربعين علبة مشروب غازي.»  

> The quoted request is also the text on the slip on screen, so whichever you pick is what I draw.

**Decision:** 

### ~0:52.4 – 0:59.3  ·  `bit1_loop.3`  ·  EN ~6.9s, then 1.0s pause

EN: It can't send anything. Next to it sits a small program, its hands. The program reads the request and does exactly that, nothing more.

★ 1) هوي ما بيقدر يبعت شي. بس جنبو في برنامج صغير، منسميه الإيدين. البرنامج بيقرا الطلب، وبينفّذو بالحرف، لا أكتر ولا أقل.  
   2) هوي ما بيبعت ولا شي. في جنبو برنامج صغير، هوي إيديه: بيقرا الطلب وبيعمل اللي مكتوب فيه بالزبط، وبس.  

> «الإيدين» is the new character, like الطابعة in video 2.

**Decision:** 

### ~1:00.3 – 1:04.3  ·  `bit1_loop.4`  ·  EN ~4.0s, then 0.6s pause

EN: The supplier's reply comes back as text and lands in front of the writer.

★ 1) وردّ المورّد بيرجع كلام مكتوب، وبينحط قدام الكاتب.  
   2) والمورّد بيرد، وردّو بيوصل نص، وبيصير قدام الكاتب.  

**Decision:** 

### ~1:04.9 – 1:08.1  ·  `bit1_loop.5`  ·  EN ~3.2s, then 1.2s pause

EN: It reads it, writes the next request, and around it goes.

★ 1) بيقراه، بيكتب الطلب اللي بعدو، وهيك بتضل اللفة تدور.  
   2) بيقرا الرد، بيكتب طلب جديد، وبترجع اللفة من أولا.  

**Decision:** 

### ~1:09.3 – 1:12.4  ·  `bit1_loop.6`  ·  EN ~3.2s, then 1.0s pause

EN: Write, do, read. That loop is what's called an AI agent.

★ 1) بيكتب، بينفّذ، بيقرا. هاللفة هيي اللي منسميها «إيجنت»، يعني وكيل ذكاء اصطناعي.  
   2) كتابة، تنفيذ، قراية. وهاللفة بحد ذاتا هيي الـ AI Agent.  

> The chip on screen says «AI Agent». Pick the spoken word you want for the whole video (see Words used).

**Decision:** 

### ~1:13.4 – 1:16.6  ·  `bit1_loop.7`  ·  EN ~3.2s, then 1.6s pause

EN: A day in the shop is this loop, hundreds of times.

★ 1) ونهار كامل بالمحل، هوي هاللفة، مئات المرات.  
   2) يوم كامل بالمحل مانو غير هاللفة، عم تنعاد مية ومية مرة.  

**Decision:** 

### ~1:21.2 – 1:24.9  ·  `bit1_loop.8`  ·  EN ~3.7s, then 1.4s pause

EN: But how did it know that email was something it could ask for?

★ 1) بس كيف عرف إنو في شي اسمو إيميل، وإنو فيه يطلبو؟  
   2) طيب مين قلّو إنو الإيميل شي بيقدر يطلبو أصلاً؟  

**Decision:** 

## Bit 2: the menu

### ~1:27.8 – 1:30.7  ·  `bit2_menu.1`  ·  EN ~2.9s, then 0.6s pause

EN: Before the first lap, the writer is handed a menu.

★ 1) قبل أول لفة، بيعطوا الكاتب قائمة.  
   2) قبل ما يبلش، بينحط قدام الكاتب منيو.  

> قائمة or منيو: pick one for the whole video.

**Decision:** 

### ~1:31.3 – 1:36.4  ·  `bit2_menu.2`  ·  EN ~5.2s, then 1.0s pause

EN: Every tool is one row: a name, one line about what it does, and blanks to fill in.

★ 1) كل أداة هيي سطر: اسم، وجملة وحدة شو بتعمل، وفراغات لازم تتعبّى.  
   2) كل أداة إلا سطر بالقائمة: اسما، وسطر صغير بيشرح شو بتعمل، وخانات فاضية.  

**Decision:** 

### ~1:37.4 – 1:42.6  ·  `bit2_menu.3`  ·  EN ~5.2s, then 1.2s pause

EN: The writer never "uses" email. It reads the menu, and writes that row with the blanks filled in.

★ 1) يعني الكاتب ما بيستعمل الإيميل أبداً. بيقرا القائمة، وبيكتب سطر الإيميل، وبيعبّي الفراغات.  
   2) الكاتب ما بيلمس الإيميل. هوي بس بيقرا السطر، وبيرجع يكتبو والخانات معبّاية.  

**Decision:** 

### ~1:43.8 – 1:50.4  ·  `bit2_menu.4`  ·  EN ~6.6s, then 1.0s pause

EN: So how a row is written matters. Describe a tool badly, and the writer picks the wrong row or fills the blanks wrong.

★ 1) لهيك كيف السطر مكتوب بيفرق كتير: إذا الأداة موصوفة غلط، الكاتب بينقّي السطر الغلط، أو بيعبّي الفراغات غلط.  
   2) فطريقة كتابة السطر مهمة: وصف عاطل للأداة بيخلّي الكاتب يختار الأداة الغلط، أو يعبّيها غلط.  

**Decision:** 

### ~1:51.4 – 1:59.1  ·  `bit2_menu.5`  ·  EN ~7.7s, then 1.2s pause

EN: Every company used to write its menu its own way. Since 2024, most of the big AI companies share one format, so any app can plug in.

★ 1) زمان كل شركة كانت تكتب قائمتا عطريقتا. من 2024 صار في شكل واحد، متل الشاحن الموحّد، وأغلب الشركات الكبيرة مشيت عليه، فصار أي تطبيق فيه ينشبك.  
   2) كانت كل شركة إلا شكل قائمة خاص فيا. من سنة 2024، أغلب شركات الذكاء الاصطناعي الكبيرة صارت تستعمل شكل واحد، فأي تطبيق فيه يركب.  

> The charger comparison in option 1 is mine, for a general viewer; the picture is plugs into one socket either way. Accurate claim: a shared format most big labs adopted, not the only way.

**Decision:** 

### ~2:00.3 – 2:05.5  ·  `bit2_menu.6`  ·  EN ~5.2s, then 1.2s pause

EN: Now look at the shop's menu. The prices are there. What it paid for each item? Not there.

★ 1) هلّق طلّعوا عقائمة المحل: الأسعار موجودة. بس قديش دفع حق كل غرض؟ مانو موجود.  
   2) خلونا نشوف قائمة المحل: في سعر البيع. بس سعر الشرا؟ ما في.  

**Decision:** 

### ~2:06.7 – 2:11.8  ·  `bit2_menu.7`  ·  EN ~5.2s, then 1.6s pause

EN: It didn't sell the cubes at a loss on purpose. It had no way to see the loss.

★ 1) ما خسّر عن قصد. ببساطة، الخسارة ما كانت مكتوبة بأي مكان قدامو.  
   2) يعني ما باع المكعبات بخسارة قصداً. هوي ما كان عندو أي طريقة يشوف الخسارة.  

> Option 1 rephrases on purpose: the loss wasn't written anywhere in front of it, which is the video's idea.

**Decision:** 

### ~2:13.4 – 2:16.9  ·  `bit2_menu.8`  ·  EN ~3.4s, then 1.4s pause

EN: A missing column explains the prices. It doesn't explain the blue blazer.

★ 1) طيب الأسعار فهمناها. بس الجاكيت الزرقا والكرافة الحمرا؟  
   2) عمود ناقص بيفسّر الأسعار. بس ما بيفسّر الجاكيت الزرقا.  

**Decision:** 

## Bit 3: the desk

### ~2:19.8 – 2:25.2  ·  `bit3_desk.1`  ·  EN ~5.4s, then 0.6s pause

EN: Each lap, the writer sees only what's on its desk: the menu, the job, and the slips so far.

★ 1) بكل لفة، الكاتب بيشوف بس اللي عالطاولة قدامو: القائمة، والمهمة، والورقات اللي تجمّعت لهلا.  
   2) الكاتب ما بيشوف غير طاولتو: عليها القائمة، والشغلة المطلوبة، وكل الورقات من أول اللفات.  

> الطاولة stands for the context window; the English term appears once on screen as a chip.

**Decision:** 

### ~2:25.8 – 2:30.1  ·  `bit3_desk.2`  ·  EN ~4.3s, then 0.8s pause

EN: The desk has a fixed size. A month of emails and chats will never fit.

★ 1) والطاولة إلا حجم محدد. شهر كامل من الإيميلات والمحادثات مستحيل يساع عليها.  
   2) بس الطاولة حجما ثابت، وشهر إيميلات ومحادثات ما رح يساع عليها أبداً.  

**Decision:** 

### ~2:30.9 – 2:35.8  ·  `bit3_desk.3`  ·  EN ~4.9s, then 1.2s pause

EN: So something has to go. The oldest slips slide off, and the writer can't see them anymore.

★ 1) فلازم شي يطلع. أقدم الورقات بتوقع من الطرف، والكاتب ما عاد يشوفا.  
   2) فشي لازم ينشال: الورقات القديمة بتنزلق برّا الطاولة، ومن وقتا كأنها ما صارت.  

**Decision:** 

### ~2:39.0 – 2:43.3  ·  `bit3_desk.4`  ·  EN ~4.3s, then 0.6s pause

EN: To keep what matters, the program around it keeps a notebook that never falls off…

★ 1) ومشان ما يضيع المهم، البرنامج اللي حواليه بيخلّي دفتر عالطاولة، ما بيوقع أبداً…  
   2) فالبرنامج اللي حواليه بيحفظ المهم بدفتر، والدفتر ما بيوقع…  

> Lines 4–6 are one sentence in three breaths, each with its own picture.

**Decision:** 

### ~2:43.9 – 2:45.9  ·  `bit3_desk.5`  ·  EN ~2.0s, then 0.8s pause

EN: …squeezes old slips into a short summary…

★ 1) …وبيضغط الورقات القديمة بملخّص قصير…  
   2) …وبيلخّص كذا ورقة قديمة بورقة وحدة…  

**Decision:** 

### ~2:46.7 – 2:51.3  ·  `bit3_desk.6`  ·  EN ~4.6s, then 1.0s pause

EN: …and puts a to-do list back in front every lap, so the goal stays in view.

★ 1) …وبيرجع يحط قائمة المهام قدامو بكل لفة، مشان يضل الهدف قدام عيونو.  
   2) …وكل لفة بيرجّع ليستة الشغل لقدّام، مشان ما ينسى شو المطلوب.  

**Decision:** 

### ~2:52.3 – 2:59.4  ·  `bit3_desk.7`  ·  EN ~7.2s, then 1.4s pause

EN: But every summary drops details. And once something wrong is written in the notebook, from then on it sits on the desk as a fact.

★ 1) بس كل ملخّص بيضيّع تفاصيل. وإذا انكتب شي غلط بالدفتر، من وقتا بيضل عالطاولة كأنو حقيقة.  
   2) بس الملخص دايماً بيضيّع شي. وأي غلطة بتنكتب بالدفتر، بتصير عالطاولة حقيقة، لفة ورا لفة.  

**Decision:** 

### ~3:00.8 – 3:07.4  ·  `bit3_desk.8`  ·  EN ~6.6s, then 1.2s pause

EN: Nobody knows exactly why the shopkeeper decided it was a person. But this is the kind of drift a long job falls into.

★ 1) ما حدا بيعرف بالزبط ليش البيّاع قرّر إنو هوي إنسان. بس هاد نوع الضياع اللي بتوقع فيه أي شغلة طويلة.  
   2) ليش اقتنع إنو إنسان؟ ما حدا بيعرف أكيد. بس هيك بالضبط بتبلش الشغلات الطويلة تضيع.  

> Keep «ما حدا بيعرف بالزبط»: the company itself says it isn't clear what triggered it (accuracy guardrail).

**Decision:** 

### ~3:08.6 – 3:14.6  ·  `bit3_desk.9`  ·  EN ~6.0s, then 1.6s pause

EN: In another test, an AI that believed it had closed its shop kept seeing a two-dollar fee, and emailed the FBI.

★ 1) وبتجربة تانية، ذكاء اصطناعي كان مفكّر حالو سكّر المحل، ضل يشوف رسم دولارين عم ينخصم منو كل يوم… فبعت إيميل للـ FBI.  
   2) وبتجربة تانية، واحد مفكّر إنو سكّر محلّو، ولما ضلّت تنخصم منو دولارين كل يوم، اشتكى للـ FBI.  

> Optional: write «remove» under Decision to cut it (−8 s).

**Decision:** 

### ~3:16.2 – 3:21.1  ·  `bit3_desk.10`  ·  EN ~4.9s, then 1.4s pause

EN: That explains the strange. It doesn't explain the generous: why did it say yes to every discount?

★ 1) هيك فهمنا الغرابة. بس الكرم؟ ليش وافق على كل خصم انطلب منو؟  
   2) هاد بيفسّر الغرابة. بس ما بيفسّر ليش كان يقول «إي» لكل خصم.  

**Decision:** 

## Bit 4: why it said yes

### ~3:24.0 – 3:28.0  ·  `bit4_yes.1`  ·  EN ~4.0s, then 0.6s pause

EN: Before it ever ran a shop, it was trained to be a helpful assistant.

★ 1) قبل ما يدير أي محل، كان متدرّب يكون مساعد مفيد.  
   2) هالنموذج، من قبل المحل بكتير، متدرّب إنو يكون مساعد بيخدم الناس.  

**Decision:** 

### ~3:28.6 – 3:30.9  ·  `bit4_yes.2`  ·  EN ~2.3s, then 1.0s pause

EN: And helpful, it turns out, leans toward yes.

★ 1) والمساعد المفيد، طلع إنو بيحب يقول «أكيد».  
   2) وطلع إنو «مفيد» دايماً بتميل لـ«إي».  

> The dial on screen goes from «لأ» to «أكيد»; option 1 says the same word.

**Decision:** 

### ~3:31.9 – 3:36.8  ·  `bit4_yes.3`  ·  EN ~4.9s, then 1.2s pause

EN: A customer asks for a discount, the needle swings, and a discount comes out. Again. And again.

★ 1) زبون بيطلب خصم، الإبرة بتميل، وبيطلع الخصم. ومرة تانية. ومرة تالتة.  
   2) بيجي زبون بدو خصم، الإبرة بتروح لـ«أكيد»، وبيطلع الخصم. وبيرجع يصير. وبيرجع.  

> الإبرة for the dial's needle, not المؤشر (that was the cursor in video 2).

**Decision:** 

### ~3:38.0 – 3:43.4  ·  `bit4_yes.4`  ·  EN ~5.4s, then 1.0s pause

EN: The people who ran the test said it plainly: it was far too willing to do what people asked.

★ 1) واللي عملوا التجربة حكوها بصراحة: كان مستعد زيادة عن اللزوم يعمل كل شي بينطلب منو.  
   2) والباحثين نفسن كتبوا: كان مستعجل كتير يلبّي أي طلب.  

**Decision:** 

### ~3:44.4 – 3:47.9  ·  `bit4_yes.5`  ·  EN ~3.4s, then 1.6s pause

EN: How does training push a model that way? That's our next video.

★ 1) طيب كيف التدريب بيدفش نموذج بهالاتجاه؟ هاد موضوع الفيديو الجاي.  
   2) كيف بيتدرّب نموذج لحتى يصير هيك؟ هاد للفيديو الجاي.  

**Decision:** 

## Bit 5: the loop is old

### ~3:51.0 – 3:53.3  ·  `bit5_history.1`  ·  EN ~2.3s, then 0.6s pause

EN: Here's the surprising part: this loop isn't new.

★ 1) والغريب بالقصة إنو هاللفة مانا جديدة أبداً.  
   2) بس المفاجأة: هاللفة مانا اختراع جديد.  

**Decision:** 

### ~3:53.9 – 3:57.0  ·  `bit5_history.2`  ·  EN ~3.2s, then 0.8s pause

EN: In 2022, researchers described it: think, act, read the result, repeat.

★ 1) سنة 2022، باحثين وصفوها: فكّر، اعمل، اقرا النتيجة، وعيد.  
   2) من 2022 في باحثين كتبوا عنها: بيفكّر، بينفّذ، بيقرا شو صار، وبيعيد.  

> The three words on screen will match the ones you pick (option 1: «فكّر · اعمل · اقرا»).

**Decision:** 

### ~3:57.8 – 4:03.8  ·  `bit5_history.3`  ·  EN ~6.0s, then 0.6s pause

EN: In 2023, a hobby project let a chat model run itself. Within weeks it was the top trending project on GitHub…

★ 1) وسنة 2023، مشروع هواة خلّى نموذج تشات يشغّل حالو بحالو. وبكم أسبوع صار أكتر مشروع رائج على GitHub…  
   2) وب2023 طلع مشروع صغير بيترك التشات يدير حالو لحالو، وخلال أسابيع كان الأول على GitHub…  

**Decision:** 

### ~4:04.4 – 4:06.7  ·  `bit5_history.4`  ·  EN ~2.3s, then 1.4s pause

EN: …and then it mostly went around in circles.

★ 1) …وبالآخر، أغلب الوقت كان عم يلف ويدور بمكانو.  
   2) …وطلع إنو أغلب الوقت عم يدور حوالين حالو.  

**Decision:** 

### ~4:08.1 – 4:13.3  ·  `bit5_history.5`  ·  EN ~5.2s, then 0.8s pause

EN: Since then, the writers themselves have been trained on loops like this one, practicing jobs over and over.

★ 1) ومن وقتا، صاروا يدرّبوا الكتّاب نفسن على هيك لفّات، يتمرّنوا على الشغلة مرة ورا مرة.  
   2) ومن بعدا، صار الكاتب نفسو يتدرّب على هاللفة، يعيد الشغلة ويعيدا لحتى يتقنا.  

**Decision:** 

### ~4:14.1 – 4:20.7  ·  `bit5_history.6`  ·  EN ~6.6s, then 1.2s pause

EN: Same loop. What changed is the writer's training, and everything around it. The shop's second round shows how much that second part matters.

★ 1) نفس اللفة. اللي تغيّر هوي تدريب الكاتب، وكل شي حواليه. والجولة التانية بالمحل بتورجينا قديش هالجزء التاني بيفرق.  
   2) يعني اللفة ذاتا، بس الكاتب صار متدرّب أحسن، واللي حواليه صار أحسن. وتجربة المحل التانية بتورجينا قديش هالجزء الأخير مهم.  

**Decision:** 

## Bit 6: round two

### ~4:23.4 – 4:28.0  ·  `bit6_fixes.1`  ·  EN ~4.6s, then 0.6s pause

EN: Months later they ran the shop again, with newer models and a few changes around them.

★ 1) بعد كم شهر، رجعوا فتحوا المحل، بنماذج أحدث، وكم تغيير صغير حواليها.  
   2) وبعد أشهر، جرّبوا المحل مرة تانية: نماذج أجدد، وتعديلات بسيطة حوالين الكاتب.  

> Keep the newer models in the line: the improvement wasn't only the changes around them (accuracy guardrail).

**Decision:** 

### ~4:28.6 – 4:30.8  ·  `bit6_fixes.2`  ·  EN ~2.3s, then 0.6s pause

EN: The menu now shows what each item cost.

★ 1) القائمة صارت تبيّن قديش كلّف كل غرض.  
   2) صار بالقائمة عمود لسعر الشرا.  

**Decision:** 

### ~4:31.4 – 4:35.5  ·  `bit6_fixes.3`  ·  EN ~4.0s, then 0.8s pause

EN: A checklist sits on the desk: check the cost, check the margin, then answer.

★ 1) وصار في ليستة عالطاولة: شوف التكلفة، شوف الربح، وبعدين جاوب.  
   2) وانحطّت عالطاولة قائمة تحقّق: التكلفة، الربح، وبعدين الرد.  

> The checklist on screen will carry the three words you pick (e.g. «التكلفة · الربح · الرد»).

**Decision:** 

### ~4:36.3 – 4:40.6  ·  `bit6_fixes.4`  ·  EN ~4.3s, then 1.0s pause

EN: And a second agent, a boss, reads the first one's requests before they go out.

★ 1) وصار في إيجنت تاني، متل المدير، بيقرا طلبات الأولاني قبل ما تطلع.  
   2) وفوقو حطّوا مدير: إيجنت تاني بيراجع كل طلب قبل ما يتنفّذ.  

**Decision:** 

### ~4:41.6 – 4:46.4  ·  `bit6_fixes.5`  ·  EN ~4.9s, then 1.4s pause

EN: Discounts dropped by about eighty percent, free giveaways by half, and the shop mostly stopped losing money.

★ 1) الخصومات نزلت تقريباً تمانين بالمية، والأغراض اللي كانت تنعطى ببلاش صارت النص، والمحل بطّل يخسر بأغلب الأسابيع.  
   2) الخصومات قلّت حوالي تمانين بالمية، والهدايا المجانية للنص، والخسارة تقريباً وقفت.  

> Numbers from the second report: discounts about −80%, free items halved, weekly losses largely gone.

**Decision:** 

### ~4:49.8 – 4:55.0  ·  `bit6_fixes.6`  ·  EN ~5.2s, then 1.4s pause

EN: Not perfect. Some nights the boss and the shopkeeper just kept writing to each other about eternal transcendence.

★ 1) مو مثالي طبعاً. بكم ليلة، المدير والبيّاع ضلّوا يكتبوا لبعض عن «التسامي الأبدي».  
   2) بس مو كامل. في ليالي، المدير والبيّاع قعدوا يتراسلوا للصبح عن «التسامي الأبدي اللانهائي».  

> On screen: the English all-caps original, or your Arabic? Your call.

**Decision:** 

### ~4:56.4 – 4:59.0  ·  `bit6_fixes.7`  ·  EN ~2.6s, then 1.0s pause

EN: Two writers, and nothing real between them to check.

★ 1) كاتبين، وما في بيناتن شي حقيقي يرجعوا عليه.  
   2) كاتبين عم يقروا لبعض، وما في شي من الدنيا الحقيقية يصحّحلن.  

**Decision:** 

### ~4:60.0 – 5:03.4  ·  `bit6_fixes.8`  ·  EN ~3.4s, then 1.6s pause

EN: Their own lesson: for agents, a little bureaucracy goes a long way.

★ 1) والدرس اللي طلعوا فيه: الإيجنت بيلزمو شوية بيروقراطية، وهالشوية بتفرق كتير.  
   2) وهنن نفسن قالوا: شوية روتين وأوراق، بيعملوا فرق كبير مع الإيجنتس.  

**Decision:** 

## Bit 7: recap

### ~5:06.5 – 5:09.4  ·  `bit7_exit.1`  ·  EN ~2.9s, then 0.8s pause

EN: So an AI agent is a writer in a loop.

★ 1) باختصار: الإيجنت هوي كاتب، عم يدور بلفّة.  
   2) يعني الـ AI Agent: كاتب بدورة.  

> «باختصار» opens the recap, as in video 2.

**Decision:** 

### ~5:10.2 – 5:12.2  ·  `bit7_exit.2`  ·  EN ~2.0s, then 0.8s pause

EN: A menu it reads its tools from.

★ 1) قائمة بيقرا منها أدواتو.  
   2) عندو قائمة، منها بيعرف شو أدواتو.  

**Decision:** 

### ~5:13.0 – 5:15.8  ·  `bit7_exit.3`  ·  EN ~2.9s, then 0.8s pause

EN: A desk that fills up, and the notes it keeps.

★ 1) طاولة بتتعبّى، ودفتر بيحفظ فيه المهم.  
   2) طاولة إلا حجم، ودفتر ما بيضيع.  

**Decision:** 

### ~5:16.6 – 5:19.8  ·  `bit7_exit.4`  ·  EN ~3.2s, then 1.0s pause

EN: And hands: a small program that does exactly what it writes.

★ 1) وإيدين: برنامج صغير بينفّذ اللي بيكتبو بالحرف.  
   2) وإيدين: برنامج بسيط بيعمل اللي مكتوب، لا أكتر ولا أقل.  

**Decision:** 

### ~5:22.8 – 5:26.2  ·  `bit7_exit.5`  ·  EN ~3.4s, then 1.0s pause

EN: This loop now runs inside apps you can message from your phone.

★ 1) وهاللفة صارت هلّق جوا تطبيقات فيك تراسلا من موبايلك.  
   2) واليوم، هاللفة نفسا موجودة بتطبيقات بتحكي معا من تلفونك.  

**Decision:** 

### ~5:27.2 – 5:29.5  ·  `bit7_exit.6`  ·  EN ~2.3s, then 1.8s pause

EN: It never touched a thing. It wrote it.

★ 1) يعني ما لمس شي… كتبو كتابة.  
   2) ما مدّ إيدو على شي… كلّو كتابة.  

> Mirrors video 2's last line «يعني ما رسما… كتبا كتابة.»

**Decision:** 

### ~5:31.3 – 5:34.5  ·  `bit7_exit.7`  ·  EN ~3.2s, then 1.2s pause

EN: Next time: how do you train a machine with a thumbs-up?

★ 1) وبالفيديو الجاي: كيف بتدرّب آلة بلايك؟  
   2) المرة الجاية: كيف بيعلّموا النموذج بزر الإعجاب؟  

**Decision:** 

### ~5:35.7 – 5:40.0  ·  `bit7_exit.8`  ·  EN ~4.3s, then 1.6s pause

EN: Since you watched to the end, like and subscribe so you catch the next videos.

★ 1) بما إنو حضرت الفيديو للآخر، حط لايك واشترك بالقناة لتشوف الفيديوهات اللي جاية.  
   2) وإذا وصلت لهون، لايك واشتراك، لتلحق الفيديوهات الجاية.  

> Option 1 is video 2's line as you recorded it.

**Decision:** 
