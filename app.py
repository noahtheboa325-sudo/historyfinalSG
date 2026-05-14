import streamlit as st
import random

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="World History Study App", page_icon="📚", layout="centered")

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

.stApp { background-color: #0f1117; color: #e8eaf6; }

.card {
    background: #1a1d27;
    border: 1px solid #2a2d3e;
    border-radius: 16px;
    padding: 28px 24px;
    margin-bottom: 16px;
    text-align: center;
}
.term { font-size: 24px; font-weight: 800; color: #6c8cff; margin-bottom: 8px; }
.def  { font-size: 15px; line-height: 1.7; color: #e8eaf6; }
.muted { color: #7b7f9e; font-size: 13px; }
.badge {
    display: inline-block;
    background: #2a2d3e;
    color: #7b7f9e;
    border-radius: 99px;
    padding: 2px 12px;
    font-size: 12px;
    margin-bottom: 20px;
}
.score-big { font-size: 52px; font-weight: 800; color: #6c8cff; text-align: center; }
.opt-correct {
    background: #1a3a2a !important;
    border: 2px solid #4caf82 !important;
    color: #4caf82 !important;
    border-radius: 10px;
    padding: 12px;
    width: 100%;
    margin-bottom: 8px;
}
.opt-wrong {
    background: #3a1a1a !important;
    border: 2px solid #ff5c72 !important;
    color: #ff5c72 !important;
    border-radius: 10px;
    padding: 12px;
    width: 100%;
    margin-bottom: 8px;
}
.match-solved {
    background: #1a2e20;
    border: 2px solid #4caf82;
    color: #4caf82;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    font-size: 12px;
    opacity: 0.6;
    min-height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.progress-bar-bg {
    background: #1a1d27;
    border-radius: 8px;
    height: 6px;
    margin-top: 16px;
    overflow: hidden;
}
.stButton > button {
    background: #6c8cff;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    padding: 8px 20px;
    transition: opacity 0.15s;
}
.stButton > button:hover { opacity: 0.85; background: #6c8cff; color: white; }
</style>
""", unsafe_allow_html=True)

# ── Data ───────────────────────────────────────────────────────────────────────
ALL_TERMS = [
    # Enlightenment
    {"term": "How does the Scientific Revolution lead to the Enlightenment?", "def": "The Scientific Revolution proved that reason and observation could uncover natural laws governing the physical world. This inspired Enlightenment thinkers to apply the same logical, rational approach to human society, government, religion, and individual rights — arguing that just as nature follows discoverable laws, so too should civilization."},
    {"term": "Natural Laws", "def": "Rules believed to govern human society and behavior, just like laws govern nature. Enlightenment thinkers argued governments should be based on these universal principles."},
    {"term": "Social Contract", "def": "The idea that people give up some freedoms to a government in exchange for protection of their remaining rights. If the government breaks this agreement, people can revolt."},
    {"term": "Hobbes", "def": "English philosopher who believed humans were naturally selfish and violent. He argued people needed a strong, authoritarian ruler to keep order — his book was called Leviathan."},
    {"term": "Locke", "def": "English philosopher who believed people were born with natural rights: life, liberty, and property. He argued governments exist to protect those rights, and people can overthrow a government that fails to do so."},
    {"term": "Philosophe", "def": "French Enlightenment thinkers who used reason to criticize society, religion, and government. They promoted ideas of freedom, justice, and progress."},
    {"term": "Voltaire", "def": "French philosophe famous for defending free speech and criticizing the Catholic Church and political tyranny. He believed in religious tolerance and reason."},
    {"term": "Montesquieu", "def": "French philosophe who proposed the separation of powers — dividing government into legislative, executive, and judicial branches to prevent any one group from having too much power."},
    {"term": "Diderot", "def": "French philosophe who created the Encyclopedia, a massive collection of Enlightenment ideas meant to spread knowledge and challenge traditional authority."},
    {"term": "Rousseau", "def": "French philosopher who believed in the general will — that government should reflect what the people as a whole want. He valued equality and popular sovereignty."},
    {"term": "Mary Wollstonecraft", "def": "British writer who argued that Enlightenment rights should apply to women too. Her book A Vindication of the Rights of Woman (1792) is an early feminist text."},
    {"term": "Adam Smith", "def": "Scottish economist who wrote The Wealth of Nations. He argued that free markets, driven by self-interest and competition, would naturally produce prosperity."},
    {"term": "Laissez Faire", "def": "French for 'let it be.' The economic idea that government should not interfere in the economy — businesses should operate freely without regulation."},
    {"term": "Censorship", "def": "Government control over what ideas can be published or spoken. Enlightenment thinkers opposed censorship and fought for freedom of the press and speech."},
    # American & French Revolution
    {"term": "American Revolution", "def": "The colonial revolt against British rule (1775–1783) inspired heavily by Enlightenment ideas. Colonists argued that Britain violated their natural rights and broke the social contract."},
    {"term": "Thomas Jefferson", "def": "Primary author of the Declaration of Independence. He drew on Locke's ideas about natural rights and the right to revolt against unjust governments."},
    {"term": "Declaration of Independence", "def": "Document written in 1776 that declared the American colonies independent from Britain. It stated that all men are created equal and have unalienable rights — life, liberty, and the pursuit of happiness."},
    {"term": "French Revolution", "def": "A period of radical political change in France (1789–1799). It overthrew the monarchy, executed the king, and eventually led to Napoleon's rise to power."},
    {"term": "Louis XVI", "def": "King of France whose weak leadership and financial mismanagement helped trigger the French Revolution. He was executed by guillotine in 1793."},
    {"term": "Jacques Necker", "def": "France's finance minister who tried to solve the debt crisis but was dismissed by Louis XVI. His firing angered Parisians and contributed to the storming of the Bastille."},
    {"term": "Marquis de Lafayette", "def": "French military hero who fought in the American Revolution, then returned to France and became a leading voice for constitutional reform during the French Revolution."},
    {"term": "Estates General", "def": "France's legislative body representing the three estates (clergy, nobility, commoners). It was called in 1789 for the first time in 175 years to address the financial crisis, which ignited revolutionary tensions."},
    {"term": "Ancien Régime", "def": "The old political and social system of France before the Revolution, dominated by the king and privileged nobles and clergy while commoners bore most of the tax burden."},
    {"term": "Deficit Spending", "def": "When a government spends more money than it collects in taxes. France's massive debts from wars (including helping the American Revolution) were a major cause of the Revolution."},
    {"term": "Tennis Court Oath", "def": "A pledge taken in 1789 by members of the Third Estate, who locked out of their meeting hall, swore not to disband until France had a new constitution."},
    {"term": "Storming of the Bastille", "def": "On July 14, 1789, Parisian crowds stormed the Bastille prison, a symbol of royal tyranny. It marked the beginning of the violent phase of the French Revolution."},
    {"term": "The Great Fear", "def": "A wave of panic and violence that swept the French countryside in summer 1789. Peasants attacked nobles' estates, fearing an aristocratic conspiracy against them."},
    {"term": "How did France's social divisions contribute to the Revolution?", "def": "France's three estates were deeply unequal. The First (clergy) and Second (nobility) Estates held privileges and paid little tax, while the Third Estate (97% of the population) bore the burden. This resentment, combined with food shortages and a financial crisis, created explosive anger that fueled the Revolution."},
    {"term": "Reign of Terror", "def": "A phase of the French Revolution (1793–1794) where the radical government executed thousands of perceived enemies of the Revolution, often without fair trials."},
    {"term": "Maximilien Robespierre", "def": "Leader of the Committee of Public Safety who directed the Reign of Terror. He believed extreme violence was necessary to protect the Revolution. Eventually he too was arrested and guillotined."},
    {"term": "Guillotine", "def": "A device used to behead people quickly, used extensively during the Reign of Terror. It became a symbol of Revolutionary violence."},
    {"term": "Why was the Committee of Public Safety allowed to terrorize France?", "def": "France was simultaneously threatened by foreign invasion and internal counter-revolutionary rebellion. The Committee convinced a frightened public that extreme measures were necessary to save the Revolution. Fear of enemies — both foreign armies and traitors within — made citizens accept and even support the violence, at least temporarily."},
    {"term": "Napoleon", "def": "French military general who rose to power after the French Revolution and became Emperor. He conquered much of Europe and spread Enlightenment legal ideas but also built an authoritarian empire."},
    {"term": "How did the turmoil of France lead to Napoleon's rise to power?", "def": "Years of revolutionary chaos, political instability, and foreign war left France desperate for strong, effective leadership. Napoleon's brilliant military victories made him a national hero. When the Directory government proved weak and corrupt, Napoleon staged a coup in 1799 (18 Brumaire), presenting himself as the man who could restore order and glory to France."},
    {"term": "Napoleonic Code", "def": "A unified legal code Napoleon established in France. It guaranteed equality before the law, property rights, and religious tolerance — but also restricted women's rights."},
    {"term": "Reforms", "def": "Napoleon introduced sweeping reforms across Europe: modernizing legal systems with the Napoleonic Code, reorganizing education, creating the Bank of France, and establishing meritocracy in government and the military. These reforms spread Enlightenment ideals of equality and rationalism, even as Napoleon ruled as an authoritarian emperor."},
    {"term": "Concert of Europe", "def": "An agreement among European powers after Napoleon's defeat to maintain the balance of power and prevent future revolutions or wars. It was established at the Congress of Vienna (1815)."},
    # Industrial Revolution
    {"term": "Entrepreneur", "def": "A person who starts and runs a business, taking on financial risk for potential profit. Entrepreneurs were key figures driving the Industrial Revolution."},
    {"term": "Capitalism", "def": "An economic system where private individuals own businesses and compete in a free market. Profit motive drives production."},
    {"term": "Capital", "def": "Money or resources invested in a business to produce goods or services."},
    {"term": "Industrial Revolution", "def": "A period of massive economic and social change (starting in Britain ~1760s) when production shifted from hand tools in homes to machines in factories."},
    {"term": "Great Britain", "def": "The first country to industrialize, due to its abundant coal and iron resources, strong navy and global trade networks, stable government, and colonies providing raw materials and markets. Its geography (no point more than 70 miles from water) also made transporting goods easy."},
    {"term": "Luddites", "def": "British workers in the early 1800s who destroyed factory machines out of fear that machinery was taking their jobs. The term now means someone who opposes new technology."},
    {"term": "Urbanization", "def": "The growth of cities as people moved from rural areas to find factory work. It led to overcrowded, often unsanitary living conditions."},
    {"term": "Standard of Living", "def": "The level of comfort and wealth available to a person or group. The Industrial Revolution raised it long-term but initially caused miserable conditions for factory workers."},
    {"term": "Communism", "def": "A political and economic system where the government owns all property and means of production on behalf of the workers. Associated with Karl Marx."},
    {"term": "Socialism", "def": "An economic system where the community or government owns and regulates the means of production, aiming to reduce inequality. Less extreme than communism."},
    {"term": "Tenements", "def": "Crowded, cheaply built urban apartment buildings where poor factory workers lived during industrialization. Conditions were often dangerous and unsanitary."},
    {"term": "Karl Marx", "def": "German philosopher and economist who wrote The Communist Manifesto (with Engels) and Das Kapital. He argued capitalism exploited workers and predicted it would eventually be overthrown."},
    {"term": "Textiles", "def": "Cloth and fabric industry — one of the first industries to be industrialized in Britain. The spinning jenny and power loom revolutionized textile production."},
    {"term": "Stocks", "def": "Shares of ownership in a company. Selling stocks allowed businesses to raise large amounts of capital to fund industrial expansion."},
    {"term": "Germ Theory", "def": "The scientific discovery that diseases are caused by microorganisms (germs), not bad air. It revolutionized medicine and public health, partly a response to urban disease outbreaks."},
    # Unification & Imperialism
    {"term": "Zollverein", "def": "A Prussian-led customs union that eliminated trade barriers between German states. It economically united Germany before political unification."},
    {"term": "Otto von Bismarck", "def": "Prussian chancellor who unified Germany through 'blood and iron' — war and political strategy rather than idealism. He used Realpolitik to achieve his goals."},
    {"term": "Realpolitik", "def": "Politics based on practical goals rather than idealistic ones. Bismarck used Realpolitik — doing whatever was necessary to increase Prussian power, regardless of ethics."},
    {"term": "Reich", "def": "German word for 'empire' or 'realm.' The First Reich was the Holy Roman Empire; the Second Reich was unified Germany under the Kaiser (1871–1918)."},
    {"term": "German Unification", "def": "The process by which Bismarck united the independent German states into one nation under Prussian leadership, completed in 1871 after the Franco-Prussian War."},
    {"term": "Kulturkampf", "def": "Bismarck's campaign ('culture struggle') to reduce Catholic Church influence in Germany. He feared the Pope's authority competed with the state's loyalty."},
    {"term": "Italian Unification", "def": "The movement to unite the Italian peninsula into one nation, achieved by 1871. Key figures included Cavour (diplomat), Garibaldi (soldier), and King Victor Emmanuel II."},
    {"term": "Nationalism in Europe", "def": "A strong belief that people with shared language, culture, or history should form their own nation-state. It was a major force driving unification in Germany and Italy and threatening multiethnic empires."},
    {"term": "Failing Empires", "def": "By the late 1800s, the Ottoman and Austro-Hungarian Empires were weakening due to nationalism — ethnic minorities wanted independence, destabilizing these multi-ethnic states."},
    {"term": "Austria-Hungary", "def": "A multiethnic empire in Central Europe that struggled to hold together as nationalist movements grew among its many ethnic groups (Slavs, Czechs, Hungarians, etc.)."},
    {"term": "New Imperialism", "def": "The period from 1870–1914 when European powers rapidly colonized Africa and Asia for resources, markets, strategic advantage, and nationalist prestige."},
    {"term": "White Man's Burden", "def": "A poem by Rudyard Kipling used to justify imperialism — the racist idea that white Europeans had a duty to 'civilize' non-white peoples. It masked exploitation with paternalism."},
    {"term": "Direct Rule", "def": "A colonial system where the imperial power controls the colony directly, replacing local leaders with its own officials."},
    {"term": "Indirect Rule", "def": "A colonial system where the imperial power governs through existing local leaders, who enforce colonial policies but maintain some local customs."},
    {"term": "Berlin Conference", "def": "A meeting of European powers (1884–1885) to divide Africa among themselves. African nations had no representation. It formalized the 'Scramble for Africa.'"},
    {"term": "King Leopold II", "def": "Belgian king who personally colonized the Congo, exploiting it for rubber and ivory while terrorizing its people. His rule caused millions of deaths and became a symbol of colonial brutality."},
    # WWI
    {"term": "Causes of WWI", "def": "The main causes are remembered as MAIN: Militarism (arms race among European powers), Alliance systems (Triple Entente vs. Triple Alliance), Imperialism (competition for colonies), and Nationalism (ethnic tensions, especially in the Balkans). The assassination of Archduke Franz Ferdinand in 1914 was the spark that ignited these underlying tensions into full-scale war."},
    {"term": "Entente", "def": "The alliance between France, Russia, and Britain (the Triple Entente). It became the core of the Allied Powers in WWI."},
    {"term": "Militarism", "def": "The glorification of military power and the aggressive buildup of armed forces. European nations competed to have the largest, most powerful militaries before WWI."},
    {"term": "Alsace and Lorraine", "def": "Two regions on the French-German border seized by Germany after the Franco-Prussian War (1871). France wanted them back, fueling tension before WWI."},
    {"term": "Mobilize", "def": "To prepare and organize a military for war. When one country mobilized, others felt they had to as well — contributing to the rapid escalation into WWI."},
    {"term": "Neutrality", "def": "A policy of not taking sides in a conflict. Several nations (like the US initially) declared neutrality at the start of WWI."},
    {"term": "Stalemate", "def": "A situation in a war where neither side can gain a decisive advantage. WWI's Western Front became a stalemate as both sides dug into trenches."},
    {"term": "Schlieffen Plan", "def": "Germany's strategy to fight a two-front war by quickly defeating France in the west, then turning to fight Russia in the east. It failed when Russia mobilized faster than expected."},
    {"term": "Allies (WWI)", "def": "France, Britain, Russia, and later the US and others. They fought against the Central Powers in WWI."},
    {"term": "Central Powers (WWI)", "def": "Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria. They fought against the Allied Powers in WWI."},
    {"term": "Trench Warfare", "def": "A style of warfare where armies dug long systems of trenches for protection. It led to a bloody stalemate on the Western Front with minimal territorial gains."},
    {"term": "Zeppelin", "def": "German airships used for bombing raids over Britain during WWI — an early example of aerial warfare targeting civilian areas."},
    {"term": "Total War", "def": "A war strategy where a country uses all its resources — economy, civilians, and military — for the war effort. Civilians became both workers and targets."},
    {"term": "Lusitania", "def": "A British ocean liner sunk by a German submarine in 1915, killing 1,198 people including Americans. It fueled anti-German sentiment and eventually helped push the US into WWI."},
    {"term": "Convoy", "def": "A system of grouping ships together with naval escorts to protect against submarine attacks. Used effectively by the Allies late in WWI."},
    {"term": "Conscription", "def": "Mandatory military service — the government forces citizens to serve in the military. Used by most major powers during WWI."},
    {"term": "Pandemic", "def": "The 1918 Spanish Flu pandemic killed 50–100 million people worldwide — more than WWI itself. Soldiers crowded in trenches and camps spread the disease rapidly."},
    {"term": "Armistice", "def": "An agreement to stop fighting. WWI ended with an armistice on November 11, 1918 (11/11 at 11am), not a total German military defeat."},
    {"term": "Treaty of Versailles", "def": "The peace treaty ending WWI (1919). It blamed Germany for the war (War Guilt Clause), imposed massive reparations, stripped Germany of territory, and limited its military. Its harsh terms fueled resentment that helped Hitler rise."},
    {"term": "WWI Death Tolls", "def": "About 17 million people died in WWI (soldiers and civilians). The scale of death shocked the world and created a strong desire to prevent future wars."},
    # Interwar & WWII
    {"term": "Collective Security", "def": "The idea that nations should work together to protect each other and prevent war — the principle behind the League of Nations and later the United Nations."},
    {"term": "United Nations", "def": "An international organization founded in 1945 to promote peace, cooperation, and human rights after WWII. It replaced the failed League of Nations."},
    {"term": "Propaganda", "def": "Information spread by governments or groups to promote a particular viewpoint or cause, often manipulating emotions. Widely used in both World Wars and the Cold War."},
    {"term": "Welfare State", "def": "A government system that takes responsibility for citizens' basic well-being through programs like unemployment insurance, healthcare, and social security."},
    {"term": "Great Depression", "def": "A global economic collapse starting with the 1929 US stock market crash. Unemployment soared, banks failed, and international trade collapsed — creating instability that helped extremist leaders rise to power."},
    {"term": "FDR", "def": "Franklin D. Roosevelt, US president during the Great Depression and most of WWII. He launched the New Deal to rescue the economy and led the US through WWII."},
    {"term": "New Deal", "def": "FDR's program of government relief, recovery, and reform to combat the Great Depression. It expanded the federal government's role in the economy and created jobs."},
    {"term": "Dust Bowl", "def": "A severe drought and dust storm crisis in the American Great Plains (1930s) that destroyed farms and displaced hundreds of thousands of families, worsening the Depression."},
    {"term": "Jazz", "def": "A uniquely American music genre born from African American culture, especially popular in the 1920s (Jazz Age). It represented cultural change, freedom, and the blending of African and European musical traditions."},
    {"term": "Russian Revolution", "def": "In 1917, Russia had two revolutions: the first overthrew the Tsar; the second brought the Bolsheviks (communists) under Lenin to power, creating the Soviet Union."},
    {"term": "Lenin", "def": "Leader of the Bolshevik Revolution. He established the Soviet Union based on Marxist ideas, ended Russia's involvement in WWI, and created a one-party communist state."},
    {"term": "Stalin", "def": "Soviet leader after Lenin who ruled through terror. He industrialized the USSR through brutal Five-Year Plans, collectivized farms (causing famine), and purged millions of people."},
    {"term": "Gulag", "def": "Soviet forced labor camps where political prisoners and 'enemies of the state' were sent under Stalin. Millions died from harsh conditions."},
    {"term": "Soviet Union", "def": "The communist state created after the Russian Revolution, officially called the USSR. It was a superpower in the Cold War and collapsed in 1991."},
    {"term": "Nazi", "def": "Members of Adolf Hitler's National Socialist German Workers' Party. Nazi ideology was based on extreme nationalism, antisemitism, and authoritarianism."},
    {"term": "Hitler", "def": "Leader of Nazi Germany who rose to power in 1933. He started WWII by invading Poland and orchestrated the Holocaust — the genocide of six million Jews and millions of others."},
    {"term": "Lebensraum", "def": "German for 'living space.' Hitler's belief that Germany needed to expand eastward to acquire territory for the German people — used to justify aggression against Poland and the USSR."},
    {"term": "Nuremberg Laws", "def": "Laws passed in Nazi Germany in 1935 that stripped Jews of citizenship and banned marriage between Jews and non-Jews — a key step in institutionalizing antisemitism."},
    {"term": "Kristallnacht", "def": "'Night of Broken Glass' (November 9–10, 1938) — a coordinated Nazi attack on Jewish homes, businesses, and synagogues. Thousands of Jews were arrested. It marked a major escalation of persecution."},
    {"term": "Holocaust", "def": "The systematic, state-sponsored genocide of six million Jews and millions of others (Roma, disabled people, political opponents, LGBTQ+ individuals) by the Nazi regime during WWII."},
    {"term": "Benito Mussolini", "def": "Fascist dictator of Italy who allied with Hitler. He promised to restore Roman-era greatness and used violence (the Black Shirts) to seize power."},
    {"term": "Black Shirts", "def": "Mussolini's paramilitary force that used violence and intimidation to crush political opposition and help him seize power in Italy in the 1920s."},
    {"term": "Fascism", "def": "An authoritarian, ultranationalist political ideology that glorifies the state and leader, suppresses opposition, and often relies on violence. Practiced by Mussolini and Hitler."},
    {"term": "Italy (WWII)", "def": "Under Mussolini, Italy allied with Nazi Germany and Japan as part of the Axis Powers. Italy invaded Ethiopia and Albania before WWII, then fought alongside Germany in North Africa and Europe. Italy switched sides to the Allies in 1943 after Mussolini was overthrown."},
    {"term": "Hideki Tojo", "def": "Japanese military leader and Prime Minister during WWII who oversaw Japanese expansion in Asia and the attack on Pearl Harbor. He was executed as a war criminal after the war."},
    {"term": "Japan (WWII)", "def": "Sought to build a Pacific empire. Invaded China and Southeast Asia, attacked Pearl Harbor in 1941, and committed atrocities like the Bataan Death March."},
    {"term": "Winston Churchill", "def": "British Prime Minister during WWII. His leadership and speeches helped Britain resist Nazi Germany during the Blitz. He refused to negotiate with Hitler."},
    {"term": "Neville Chamberlain", "def": "British PM before Churchill. Known for appeasement — giving Hitler territory (Sudetenland, 1938) to avoid war. It failed and emboldened Hitler."},
    {"term": "European Theater", "def": "The areas of WWII combat in Europe and North Africa. Key events included D-Day (1944), the Battle of the Bulge, and the fall of Berlin."},
    {"term": "Blitzkrieg", "def": "German for 'lightning war.' A rapid military strategy using tanks, planes, and infantry in coordinated attacks to overwhelm enemies quickly before they could respond."},
    {"term": "Pacific Theater", "def": "The areas of WWII combat in the Pacific Ocean and Asia. Key events include Pearl Harbor, island-hopping campaigns, and the use of atomic bombs on Japan."},
    {"term": "Bataan Death March", "def": "After the fall of the Philippines in 1942, Japanese forces forced 70,000+ American and Filipino POWs to march 65 miles in brutal heat. Thousands died from abuse, starvation, and disease."},
    {"term": "Ending the War", "def": "WWII ended in Europe on V-E Day (May 8, 1945) after Germany's surrender, and in the Pacific on V-J Day (August 15, 1945) after the US dropped atomic bombs on Hiroshima and Nagasaki."},
    {"term": "A-Bomb", "def": "The atomic bombs dropped on Hiroshima (Aug. 6, 1945) and Nagasaki (Aug. 9, 1945). Each killed tens of thousands instantly and ended WWII — but opened the nuclear age and debates about civilian targeting."},
    {"term": "Repercussions of WWII", "def": "WWII reshaped the world: the US and USSR emerged as superpowers, Europe was divided, the UN was created, Israel was founded, the Cold War began, and decolonization accelerated."},
    # Cold War
    {"term": "Cold War", "def": "A state of geopolitical tension (1947–1991) between the US (capitalism/democracy) and the USSR (communism) that never escalated into direct military conflict but shaped global politics."},
    {"term": "Truman Doctrine", "def": "President Truman's 1947 policy pledging US support to countries threatened by communist takeover. It was first applied to Greece and Turkey."},
    {"term": "Containment", "def": "The US foreign policy strategy of preventing communism from spreading to new countries. Shaped US involvement in Korea, Vietnam, and elsewhere during the Cold War."},
    {"term": "Marshall Plan", "def": "US program (1948) that provided economic aid to rebuild Western European countries after WWII. It aimed to prevent poverty from making communist takeover more appealing."},
    {"term": "Berlin Airlift", "def": "When the USSR blockaded West Berlin in 1948, the US and Britain flew in supplies for 11 months until the Soviets lifted the blockade. A major early Cold War victory for the West."},
    {"term": "Iron Curtain", "def": "Churchill's term for the boundary dividing communist Eastern Europe from democratic Western Europe during the Cold War."},
    {"term": "Berlin Wall", "def": "A wall built by East Germany in 1961 to stop citizens from fleeing to West Berlin. It became the most powerful symbol of Cold War division. It fell in 1989."},
    {"term": "NATO", "def": "North Atlantic Treaty Organization — a military alliance formed in 1949 by Western nations pledging mutual defense. Created in response to Soviet expansionism."},
    {"term": "Mutually Assured Destruction (MAD)", "def": "The Cold War doctrine that both the US and USSR had enough nuclear weapons to destroy each other — meaning neither would launch first, because it would guarantee their own annihilation."},
    {"term": "Military Industrial Complex", "def": "President Eisenhower's term for the powerful relationship between the US military and the defense industry. He warned it could gain undue political influence."},
    {"term": "Discrimination", "def": "Treating people unfairly based on characteristics like race, gender, or religion. During the Cold War, US racial inequality was used by the USSR as propaganda against American democracy."},
    {"term": "Segregation", "def": "The forced separation of races, especially in the American South. The Civil Rights Movement fought against legal segregation, culminating in the Civil Rights Act of 1964."},
    {"term": "Margaret Thatcher", "def": "British Prime Minister (1979–1990) who promoted free-market economics (Thatcherism), reduced government spending, and privatized industries. A major conservative leader of the Cold War era."},
    {"term": "GDP (Gross Domestic Product)", "def": "The total value of all goods and services produced in a country in a year. Used to measure the size and health of an economy."},
    {"term": "Fidel Castro", "def": "Communist revolutionary who took control of Cuba in 1959. His alliance with the USSR made Cuba a Cold War flashpoint, especially during the Cuban Missile Crisis."},
    {"term": "John F. Kennedy", "def": "US President (1961–1963) who navigated the Cuban Missile Crisis, pledged to defend Berlin, and escalated early US involvement in Vietnam before his assassination."},
    {"term": "Lyndon B. Johnson", "def": "US President after JFK who dramatically escalated the Vietnam War and also passed major civil rights legislation (Civil Rights Act 1964, Voting Rights Act 1965)."},
    {"term": "Cuban Missile Crisis", "def": "A 13-day standoff in 1962 when the US discovered Soviet nuclear missiles in Cuba. Kennedy and Khrushchev negotiated — the Soviets withdrew missiles, the US promised not to invade Cuba. The closest the Cold War came to nuclear war."},
    {"term": "Vietnam War", "def": "US military involvement (1955–1975) to prevent communist North Vietnam from taking over South Vietnam. The US withdrew after massive protest and casualties. North Vietnam won."},
    {"term": "Tet Offensive", "def": "A massive 1968 coordinated attack by North Vietnamese and Viet Cong forces on South Vietnamese cities during the Tet holiday. It shocked Americans who were told the US was winning the war."},
    {"term": "Domino Theory", "def": "The Cold War belief that if one country fell to communism, neighboring countries would follow like dominoes. Used to justify US involvement in Korea and Vietnam."},
    {"term": "Ho Chi Minh", "def": "Communist leader of North Vietnam who led the fight to unify Vietnam under communism. He was inspired by nationalism as much as Marxism and is considered a national hero in Vietnam."},
]

UNITS = {
    "All Terms": None,
    "Enlightenment": [
        "How does the Scientific Revolution lead to the Enlightenment?",
        "Natural Laws","Social Contract","Hobbes","Locke","Philosophe","Voltaire","Montesquieu",
        "Diderot","Rousseau","Mary Wollstonecraft","Adam Smith","Laissez Faire","Censorship"
    ],
    "American & French Revolution": [
        "American Revolution","Thomas Jefferson","Declaration of Independence","French Revolution",
        "Louis XVI","Jacques Necker","Marquis de Lafayette","Estates General","Ancien Régime",
        "Deficit Spending","Tennis Court Oath","Storming of the Bastille","The Great Fear",
        "How did France's social divisions contribute to the Revolution?",
        "Reign of Terror","Maximilien Robespierre","Guillotine",
        "Why was the Committee of Public Safety allowed to terrorize France?",
        "Napoleon","How did the turmoil of France lead to Napoleon's rise to power?",
        "Napoleonic Code","Reforms","Concert of Europe"
    ],
    "Industrial Revolution": [
        "Entrepreneur","Capitalism","Capital","Industrial Revolution","Great Britain",
        "Luddites","Urbanization","Standard of Living","Communism","Socialism","Tenements",
        "Karl Marx","Textiles","Stocks","Germ Theory"
    ],
    "Unification & Imperialism": [
        "Zollverein","Otto von Bismarck","Realpolitik","Reich","German Unification","Kulturkampf",
        "Italian Unification","Nationalism in Europe","Failing Empires","Austria-Hungary",
        "New Imperialism","White Man's Burden","Direct Rule","Indirect Rule",
        "Berlin Conference","King Leopold II"
    ],
    "WWI": [
        "Causes of WWI","Entente","Militarism","Alsace and Lorraine","Mobilize","Neutrality",
        "Stalemate","Schlieffen Plan","Allies (WWI)","Central Powers (WWI)","Trench Warfare",
        "Zeppelin","Total War","Lusitania","Convoy","Conscription","Pandemic","Armistice",
        "Treaty of Versailles","WWI Death Tolls"
    ],
    "Interwar & WWII": [
        "Collective Security","United Nations","Propaganda","Welfare State","Great Depression",
        "FDR","New Deal","Dust Bowl","Jazz","Russian Revolution","Lenin","Stalin","Gulag",
        "Soviet Union","Nazi","Hitler","Lebensraum","Nuremberg Laws","Kristallnacht","Holocaust",
        "Benito Mussolini","Black Shirts","Fascism","Italy (WWII)","Hideki Tojo","Japan (WWII)",
        "Winston Churchill","Neville Chamberlain","European Theater","Blitzkrieg","Pacific Theater",
        "Bataan Death March","Ending the War","A-Bomb","Repercussions of WWII"
    ],
    "Cold War": [
        "Cold War","Truman Doctrine","Containment","Marshall Plan","Berlin Airlift","Iron Curtain",
        "Berlin Wall","NATO","Mutually Assured Destruction (MAD)","Military Industrial Complex",
        "Discrimination","Segregation","Margaret Thatcher","GDP (Gross Domestic Product)",
        "Fidel Castro","John F. Kennedy","Lyndon B. Johnson","Cuban Missile Crisis","Vietnam War",
        "Tet Offensive","Domino Theory","Ho Chi Minh"
    ],
}

def get_terms(unit_name):
    if UNITS[unit_name] is None:
        return ALL_TERMS
    names = set(UNITS[unit_name])
    return [t for t in ALL_TERMS if t["term"] in names]
