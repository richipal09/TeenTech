import streamlit as st
import webbrowser

st.title("The Semantics")

st.markdown("---")
st.header("Our Mission:")
st.write("Welcome Semantics, we need your skills to figure out what motive is causing catastrophe!")
st.write("Our Agents have collected a series of conversations and encrypted them!")
st.write("Navigate through the transcripts - find the motive behind the catastrophe!")
st.write("Use the keywords on the right to help inform your decision - You have three chances to decrypt the relevant transcript!")
st.write("Use the notes section to track your thoughts!")
st.write("Good Luck Agents!")

transcript_1_content = """
**Receptionist:** dovresti iniziare a esaminare la carne coltivata in laboratorio.  
**Assistente:** Non mi fido di loro, non credo sia giusto.  
**Receptionist:** È meglio di quello che facciamo ora, allineando tutti quegli animali da macellare.  
**Assistente:** Sono d'accordo che dobbiamo fare qualcosa di diverso, ma questa scienza non sta andando troppo oltre.  
**Assistente:** Grown living tissue in a test tube per essere cucinato in seguito.  
**Receptionist:** Se l'accumulo di nutrienti è lo stesso, quale differenza fa, non può sentire dolore.  
**Assistente:** Beh no, non può che dire questo di noi e del nostro distacco dalla natura.  
**Receptionist:** Meglio staccarsi e fermare il nostro abuso della natura, la sua barbarie nelle batterie.  
**Assistente:** Penso solo che dovremmo guardare a stili di vita alternativi che sono meno centrati sulla carne.  
**Receptionist:** Ma la carne sarà ancora parte dello stile di vita, quindi l'uccisione continua.  
**Assistente:** Questo è vero, ma non dovrebbe essere su scala industriale.  
**Receptionist:** possiamo aspettare e vedere.  
"""
transcript_2_content = """
**Ασθενής:** Σας ευχαριστώ που με είδατε.  Σε παρακαλώ, μπορείς να βοηθήσεις, δεν ξέρω τι συμβαίνει με μένα.  
**Επίσημος:** Ω, αγαπητέ, ποιο φαίνεται να είναι το πρόβλημα;  
**Ασθενής:** Λοιπόν, κάτι δεν είναι σωστό και δεν μπορώ να καταλάβω ακριβώς τι είναι.  
**Υπάλληλος:** Λυπάμαι που το ακούω.  Πόσο καιρό συμβαίνει αυτό;  
**Ασθενής:** Εδώ και αρκετές εβδομάδες.  
**Επίσημος:** Εντάξει, ας δούμε αν μπορώ να σας βοηθήσω.   Γιατί πιστεύετε ότι κάτι δεν πάει καλά;  
**Ασθενής:** Λοιπόν, έχω αυτόν τον πόνο και δεν μπορώ να γυμναστώ αν είναι στο γόνατό μου, στο μηρό μου ή στην πλάτη μου.  
**Επίσημος:** Χμμ, αν είμαι ειλικρινής, νομίζω ότι το πρόβλημα μπορεί να είναι με τα μάτια σας.  
**Ασθενής:** Γιατί το πιστεύετε αυτό;  
**Επίσημος:** Λοιπόν, αυτό δεν είναι χειρουργική επέμβαση γιατρού, είναι τράπεζα!
"""

transcript_3_content = """
**Office Manager:** Ah Amanda, blij dat je hier bent, ik heb bijna een uur gewacht!  
**IT-technicus:** Ja, je ticket werd door het systeem niet als kritiek beschouwd.  
**Office Manager:** Oh nee, waarom? Ik moet deze verslagen vandaag boven hebben!  
**IT-technicus:** Als dat het geval was, had je het moeten escaleren, managers krijgen niet automatisch prioriteit.  
**IT-technicus:** Laten we eens kijken. Moet je rapporten afdrukken?  
**Office Manager:** Ja, 5 van hen en ze zijn 10 pagina's elk.  
**IT-technicus:** Nou, ik heb het papier en de inkt gecontroleerd. Het is klaar om te gaan.  
**Office Manager:** Stuur het opnieuw... Niets zien. Is het omdat het regent?  
**IT-technicus:** regen? waarom zou dat effect hebben?  
**Office Manager:** Elektriciteit en water mengen niet, ik weet het niet!  
**IT-technicus:** Dat zal het niet zijn, geloof me.  
**Technicus:** Oh mijn god.  
**Office Manager:** Wat, heb je het opgelost?  
**IT-technicus:** Ja, je was aan het afdrukken als PDF, niet vanaf de printer.  
**Kantoormanager:** Ah.
"""

transcript_4_content = """
**Responsable de operaciones:** ¿Hola Victor? Señor? Tenemos un problema.  
**CEO:** ¿Vatios? Espero que por tu bien este problema valga la pena interrumpir mi viaje de golf.  
**Responsable de operaciones:** Se trata de nuestra planta, está bajo investigación para el sitio de eliminación de residuos mineros.  
**CEO:** Sí. Desechamos los residuos, llegamos al punto en que estoy en la calle.  
**Líder de Operaciones:** Bueno, nuestra salida es ilegal. El contenido de los residuos es peligroso, nos cerrarán.  
**CEO:** Ugh!, Bogey. Eso fue tu culpa Watts... bueno, deja que nos cierren, no ralentizará la producción.  
**Líder de operaciones:** Pero qué haremos con las aguas residuales, la cantidad de almacenamiento llamaría la atención.  
**CEO:** ¡Podemos venderlo! Por supuesto.  
**Pista de operaciones:** Disculpas señor, pero las aguas residuales son tóxicas que nunca estarían de acuerdo con esto.  
**CEO:** No los necesitamos, esta no sería la primera vez que "persuadimos" a algunos concejales.
"""

transcript_5_content = """
**导师:** 苏珊，你是怎么找到新职位的？终于有了自己的团队！  
**Mentee:** 是的！早安，杰克。我很感激你的支持，如果没有你的帮助，我永远不会有信心把我的名字放在那里  
**导师:** 你做得很好，你被驱使去支持你周围的人。这些都是有价值的特征。  
**Mentee:** 我只是担心我无法处理困难的人物，我注意到我不是很同情。  
**导师:** 不是同情？你能给我举个例子，让我能理解你的同情心吗？  
**Mentee:** 一个例子。所以之前在团队工作，上个季度，科林一直在努力工作，但我们没有资源来帮助，这是压倒他的。但因为我们不能做任何事情来帮助他，我只是告诉他“这是什么”，并达到截止日期。他没有感觉好多了，但最后期限已经到了。  
**导师:** 是的，我明白了，所以即使他感到压力，他仍然能够实现目标。问题是，他花了那段时间不知所措和恐慌，当他本可以平静和放心。  
**Mentee:** 确切地说，现在我需要为整个团队做到这一点，这对我来说并不自然。我只是想要一个无稽之谈的团队。  
**导师:** 恐怕这是赚来的，如果你的团队看到你为他们努力工作，真正关心他们的福祉，他们会为你做同样的事情。仅仅因为目标被击中，这并不意味着你的工作完成了。能够与同事建立联系并了解他们的观点至关重要。让我们在下一节中讨论一下这样的情况，同时思考一下。但别担心，有足够的时间来学习。
"""

col1, col2, col3, col4, col5 = st.columns(5)  

with col1:
    if st.button("Transcript 1"):
        st.session_state.selected_transcript = transcript_1_content

with col2:
    if st.button("Transcript 2"):
        st.session_state.selected_transcript = transcript_2_content

with col3:
    if st.button("Transcript 3"):
        st.session_state.selected_transcript = transcript_3_content

with col4:
    if st.button("Transcript 4"):
        st.session_state.selected_transcript = transcript_4_content

with col5:
    if st.button("Transcript 5"):
        st.session_state.selected_transcript = transcript_5_content

if "selected_transcript" in st.session_state:
    st.markdown("---")
    st.markdown(st.session_state.selected_transcript)

    col_left, col_right = st.columns(2) 
    
    with col_left:
        if st.button("Translate"):
            webbrowser.open("https://aiservicesdemo.oraclecorp.com/demos/language/translation")

    with col_right:
        if st.button("Analyse"):
            webbrowser.open("https://aiservicesdemo.oraclecorp.com/demos/language/text-analytics")

st.markdown("---")
st.header("Notes")
notes = st.text_area("Write your notes here:")

if notes:
    st.write("Your notes:", notes)