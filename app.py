import { useState, useEffect } from "react";

const allTerms = [
  // Scientific Revolution & Enlightenment
  { term: "Scientific Revolution → Enlightenment", def: "The Scientific Revolution showed that reason and observation could uncover natural laws. This inspired Enlightenment thinkers to apply the same logical thinking to society, government, and human rights." },
  { term: "Natural Laws", def: "Rules believed to govern human society and behavior, just like laws govern nature. Enlightenment thinkers argued governments should be based on these universal principles." },
  { term: "Social Contract", def: "The idea that people give up some freedoms to a government in exchange for protection of their remaining rights. If the government breaks this agreement, people can revolt." },
  { term: "Hobbes", def: "English philosopher who believed humans were naturally selfish and violent. He argued people needed a strong, authoritarian ruler to keep order — his book was called Leviathan." },
  { term: "Locke", def: "English philosopher who believed people were born with natural rights: life, liberty, and property. He argued governments exist to protect those rights, and people can overthrow a government that fails to do so." },
  { term: "Philosophe", def: "French Enlightenment thinkers who used reason to criticize society, religion, and government. They promoted ideas of freedom, justice, and progress." },
  { term: "Voltaire", def: "French philosophe famous for defending free speech and criticizing the Catholic Church and political tyranny. He believed in religious tolerance and reason." },
  { term: "Montesquieu", def: "French philosophe who proposed the separation of powers — dividing government into legislative, executive, and judicial branches to prevent any one group from having too much power." },
  { term: "Diderot", def: "French philosophe who created the Encyclopedia, a massive collection of Enlightenment ideas meant to spread knowledge and challenge traditional authority." },
  { term: "Rousseau", def: "French philosopher who believed in the general will — that government should reflect what the people as a whole want. He valued equality and popular sovereignty." },
  { term: "Mary Wollstonecraft", def: "British writer who argued that Enlightenment rights should apply to women too. Her book A Vindication of the Rights of Woman (1792) is an early feminist text." },
  { term: "Adam Smith", def: "Scottish economist who wrote The Wealth of Nations. He argued that free markets, driven by self-interest and competition, would naturally produce prosperity." },
  { term: "Laissez Faire", def: "French for 'let it be.' The economic idea that government should not interfere in the economy — businesses should operate freely without regulation." },
  { term: "Censorship", def: "Government control over what ideas can be published or spoken. Enlightenment thinkers opposed censorship and fought for freedom of the press and speech." },

  // American Revolution
  { term: "American Revolution", def: "The colonial revolt against British rule (1775–1783) inspired heavily by Enlightenment ideas. Colonists argued that Britain violated their natural rights and broke the social contract." },
  { term: "Thomas Jefferson", def: "Primary author of the Declaration of Independence. He drew on Locke's ideas about natural rights and the right to revolt against unjust governments." },
  { term: "Declaration of Independence", def: "Document written in 1776 that declared the American colonies independent from Britain. It stated that all men are created equal and have unalienable rights — life, liberty, and the pursuit of happiness." },

  // French Revolution
  { term: "French Revolution", def: "A period of radical political change in France (1789–1799). It overthrew the monarchy, executed the king, and eventually led to Napoleon's rise to power." },
  { term: "Louis XVI", def: "King of France whose weak leadership and financial mismanagement helped trigger the French Revolution. He was executed by guillotine in 1793." },
  { term: "Jacques Necker", def: "France's finance minister who tried to solve the debt crisis but was dismissed by Louis XVI. His firing angered Parisians and contributed to the storming of the Bastille." },
  { term: "Marquis de Lafayette", def: "French military hero who fought in the American Revolution, then returned to France and became a leading voice for constitutional reform during the French Revolution." },
  { term: "Estates General", def: "France's legislative body representing the three estates (clergy, nobility, commoners). It was called in 1789 for the first time in 175 years to address the financial crisis, which ignited revolutionary tensions." },
  { term: "Ancien Régime", def: "The old political and social system of France before the Revolution, dominated by the king and privileged nobles and clergy while commoners bore most of the tax burden." },
  { term: "Deficit Spending", def: "When a government spends more money than it collects in taxes. France's massive debts from wars (including helping the American Revolution) were a major cause of the Revolution." },
  { term: "Tennis Court Oath", def: "A pledge taken in 1789 by members of the Third Estate, who locked out of their meeting hall, swore not to disband until France had a new constitution." },
  { term: "Storming of the Bastille", def: "On July 14, 1789, Parisian crowds stormed the Bastille prison, a symbol of royal tyranny. It marked the beginning of the violent phase of the French Revolution." },
  { term: "The Great Fear", def: "A wave of panic and violence that swept the French countryside in summer 1789. Peasants attacked nobles' estates, fearing an aristocratic conspiracy against them." },
  { term: "Social Divisions & the Revolution", def: "France's three estates were deeply unequal. The First (clergy) and Second (nobility) Estates held privileges and paid little tax, while the Third Estate (97% of the population) bore the burden — this resentment fueled revolution." },
  { term: "Reign of Terror", def: "A phase of the French Revolution (1793–1794) where the radical government executed thousands of perceived enemies of the Revolution, often without fair trials." },
  { term: "Maximilien Robespierre", def: "Leader of the Committee of Public Safety who directed the Reign of Terror. He believed extreme violence was necessary to protect the Revolution. Eventually he too was arrested and guillotined." },
  { term: "Guillotine", def: "A device used to behead people quickly, used extensively during the Reign of Terror. It became a symbol of Revolutionary violence." },
  { term: "Why the Terror Was Allowed", def: "France was threatened by foreign invasion and internal rebellion. The Committee convinced the public that harsh measures were necessary to save the Revolution — fear of enemies made people accept the violence." },

  // Napoleon
  { term: "Napoleon", def: "French military general who rose to power after the French Revolution and became Emperor. He conquered much of Europe and spread Enlightenment legal ideas but also built an authoritarian empire." },
  { term: "Napoleon's Rise", def: "The chaos of the Revolution left France unstable and desperate for strong leadership. Napoleon's military victories made him a hero. He staged a coup in 1799 and took control of the government." },
  { term: "Napoleonic Code", def: "A unified legal code Napoleon established in France. It guaranteed equality before the law, property rights, and religious tolerance — but also restricted women's rights." },
  { term: "Concert of Europe", def: "An agreement among European powers after Napoleon's defeat to maintain the balance of power and prevent future revolutions or wars. It was established at the Congress of Vienna (1815)." },

  // Industrial Revolution
  { term: "Entrepreneur", def: "A person who starts and runs a business, taking on financial risk for potential profit. Entrepreneurs were key figures driving the Industrial Revolution." },
  { term: "Capitalism", def: "An economic system where private individuals own businesses and compete in a free market. Profit motive drives production." },
  { term: "Capital", def: "Money or resources invested in a business to produce goods or services." },
  { term: "Industrial Revolution", def: "A period of massive economic and social change (starting in Britain ~1760s) when production shifted from hand tools in homes to machines in factories." },
  { term: "Great Britain (Industrial Rev.)", def: "The first country to industrialize due to its coal and iron resources, strong navy and trade, stable government, and colonies providing raw materials." },
  { term: "Luddites", def: "British workers in the early 1800s who destroyed factory machines out of fear that machinery was taking their jobs. The term now means someone who opposes new technology." },
  { term: "Urbanization", def: "The growth of cities as people moved from rural areas to find factory work. It led to overcrowded, often unsanitary living conditions." },
  { term: "Standard of Living", def: "The level of comfort and wealth available to a person or group. The Industrial Revolution raised it long-term but initially caused miserable conditions for factory workers." },
  { term: "Communism", def: "A political and economic system where the government owns all property and means of production on behalf of the workers. Associated with Karl Marx." },
  { term: "Socialism", def: "An economic system where the community or government owns and regulates the means of production, aiming to reduce inequality. Less extreme than communism." },
  { term: "Tenements", def: "Crowded, cheaply built urban apartment buildings where poor factory workers lived during industrialization. Conditions were often dangerous and unsanitary." },
  { term: "Karl Marx", def: "German philosopher and economist who wrote The Communist Manifesto (with Engels) and Das Kapital. He argued capitalism exploited workers and predicted it would eventually be overthrown." },
  { term: "Textiles", def: "Cloth and fabric industry — one of the first industries to be industrialized in Britain. The spinning jenny and power loom revolutionized textile production." },
  { term: "Stocks", def: "Shares of ownership in a company. Selling stocks allowed businesses to raise large amounts of capital to fund industrial expansion." },
  { term: "Germ Theory", def: "The scientific discovery that diseases are caused by microorganisms (germs), not bad air. It revolutionized medicine and public health, partly a response to urban disease outbreaks." },

  // German & Italian Unification
  { term: "Zollverein", def: "A Prussian-led customs union that eliminated trade barriers between German states. It economically united Germany before political unification." },
  { term: "Otto von Bismarck", def: "Prussian chancellor who unified Germany through 'blood and iron' — war and political strategy rather than idealism. He used Realpolitik to achieve his goals." },
  { term: "Realpolitik", def: "Politics based on practical goals rather than idealistic ones. Bismarck used Realpolitik — doing whatever was necessary to increase Prussian power, regardless of ethics." },
  { term: "Reich", def: "German word for 'empire' or 'realm.' The First Reich was the Holy Roman Empire; the Second Reich was unified Germany under the Kaiser (1871–1918)." },
  { term: "German Unification", def: "The process by which Bismarck united the independent German states into one nation under Prussian leadership, completed in 1871 after the Franco-Prussian War." },
  { term: "Kulturkampf", def: "Bismarck's campaign ('culture struggle') to reduce Catholic Church influence in Germany. He feared the Pope's authority competed with the state's loyalty." },
  { term: "Italian Unification", def: "The movement to unite the Italian peninsula into one nation, achieved by 1871. Key figures included Cavour (diplomat), Garibaldi (soldier), and King Victor Emmanuel II." },
  { term: "Nationalism in Europe", def: "A strong belief that people with shared language, culture, or history should form their own nation-state. It was a major force driving unification in Germany and Italy and threatening multiethnic empires." },
  { term: "Failing Empires", def: "By the late 1800s, the Ottoman and Austro-Hungarian Empires were weakening due to nationalism — ethnic minorities wanted independence, destabilizing these multi-ethnic states." },
  { term: "Austria-Hungary", def: "A multiethnic empire in Central Europe that struggled to hold together as nationalist movements grew among its many ethnic groups (Slavs, Czechs, Hungarians, etc.)." },

  // Imperialism
  { term: "New Imperialism", def: "The period from 1870–1914 when European powers rapidly colonized Africa and Asia for resources, markets, strategic advantage, and nationalist prestige." },
  { term: "White Man's Burden", def: "A poem by Rudyard Kipling used to justify imperialism — the racist idea that white Europeans had a duty to 'civilize' non-white peoples. It masked exploitation with paternalism." },
  { term: "Direct Rule", def: "A colonial system where the imperial power controls the colony directly, replacing local leaders with its own officials." },
  { term: "Indirect Rule", def: "A colonial system where the imperial power governs through existing local leaders, who enforce colonial policies but maintain some local customs." },
  { term: "Berlin Conference", def: "A meeting of European powers (1884–1885) to divide Africa among themselves. African nations had no representation. It formalized the 'Scramble for Africa.'" },
  { term: "King Leopold II", def: "Belgian king who personally colonized the Congo, exploiting it for rubber and ivory while terrorizing its people. His rule caused millions of deaths and became a symbol of colonial brutality." },

  // WWI
  { term: "Causes of WWI (MAIN)", def: "Militarism, Alliance systems, Imperialism, and Nationalism. The assassination of Archduke Franz Ferdinand in 1914 was the spark that set off these underlying tensions." },
  { term: "Entente", def: "The alliance between France, Russia, and Britain (the Triple Entente). It became the core of the Allied Powers in WWI." },
  { term: "Militarism", def: "The glorification of military power and the aggressive buildup of armed forces. European nations competed to have the largest, most powerful militaries before WWI." },
  { term: "Alsace and Lorraine", def: "Two regions on the French-German border seized by Germany after the Franco-Prussian War (1871). France wanted them back, fueling tension before WWI." },
  { term: "Mobilize", def: "To prepare and organize a military for war. When one country mobilized, others felt they had to as well — contributing to the rapid escalation into WWI." },
  { term: "Neutrality", def: "A policy of not taking sides in a conflict. Several nations (like the US initially) declared neutrality at the start of WWI." },
  { term: "Stalemate", def: "A situation in a war where neither side can gain a decisive advantage. WWI's Western Front became a stalemate as both sides dug into trenches." },
  { term: "Schlieffen Plan", def: "Germany's strategy to fight a two-front war by quickly defeating France in the west, then turning to fight Russia in the east. It failed when Russia mobilized faster than expected." },
  { term: "Allies (WWI)", def: "France, Britain, Russia, and later the US and others. They fought against the Central Powers in WWI." },
  { term: "Central Powers (WWI)", def: "Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria. They fought against the Allied Powers in WWI." },
  { term: "Trench Warfare", def: "A style of warfare where armies dug long systems of trenches for protection. It led to a bloody stalemate on the Western Front with minimal territorial gains." },
  { term: "Zeppelin", def: "German airships used for bombing raids over Britain during WWI — an early example of aerial warfare targeting civilian areas." },
  { term: "Total War", def: "A war strategy where a country uses all its resources — economy, civilians, and military — for the war effort. Civilians became both workers and targets." },
  { term: "Lusitania", def: "A British ocean liner sunk by a German submarine in 1915, killing 1,198 people including Americans. It fueled anti-German sentiment and eventually helped push the US into WWI." },
  { term: "Convoy", def: "A system of grouping ships together with naval escorts to protect against submarine attacks. Used effectively by the Allies late in WWI." },
  { term: "Conscription", def: "Mandatory military service — the government forces citizens to serve in the military. Used by most major powers during WWI." },
  { term: "Pandemic", def: "The 1918 Spanish Flu pandemic killed 50–100 million people worldwide — more than WWI itself. Soldiers crowded in trenches and camps spread the disease rapidly." },
  { term: "Armistice", def: "An agreement to stop fighting. WWI ended with an armistice on November 11, 1918 (11/11 at 11am), not a total German military defeat." },
  { term: "Treaty of Versailles", def: "The peace treaty ending WWI (1919). It blamed Germany for the war (War Guilt Clause), imposed massive reparations, stripped Germany of territory, and limited its military. Its harsh terms fueled resentment that helped Hitler rise." },
  { term: "WWI Death Tolls", def: "About 17 million people died in WWI (soldiers and civilians). The scale of death shocked the world and created a strong desire to prevent future wars." },

  // Interwar Period
  { term: "Collective Security", def: "The idea that nations should work together to protect each other and prevent war — the principle behind the League of Nations and later the United Nations." },
  { term: "United Nations", def: "An international organization founded in 1945 to promote peace, cooperation, and human rights after WWII. It replaced the failed League of Nations." },
  { term: "Propaganda", def: "Information spread by governments or groups to promote a particular viewpoint or cause, often manipulating emotions. Widely used in both World Wars and the Cold War." },
  { term: "Welfare State", def: "A government system that takes responsibility for citizens' basic well-being through programs like unemployment insurance, healthcare, and social security." },
  { term: "Great Depression", def: "A global economic collapse starting with the 1929 US stock market crash. Unemployment soared, banks failed, and international trade collapsed — creating instability that helped extremist leaders rise to power." },
  { term: "FDR", def: "Franklin D. Roosevelt, US president during the Great Depression and most of WWII. He launched the New Deal to rescue the economy and led the US through WWII." },
  { term: "New Deal", def: "FDR's program of government relief, recovery, and reform to combat the Great Depression. It expanded the federal government's role in the economy and created jobs." },
  { term: "Dust Bowl", def: "A severe drought and dust storm crisis in the American Great Plains (1930s) that destroyed farms and displaced hundreds of thousands of families, worsening the Depression." },
  { term: "Jazz", def: "A uniquely American music genre born from African American culture, especially popular in the 1920s (Jazz Age). It represented cultural change, freedom, and the blending of African and European musical traditions." },

  // Russian Revolution
  { term: "Russian Revolution", def: "In 1917, Russia had two revolutions: the first overthrew the Tsar; the second brought the Bolsheviks (communists) under Lenin to power, creating the Soviet Union." },
  { term: "Lenin", def: "Leader of the Bolshevik Revolution. He established the Soviet Union based on Marxist ideas, ended Russia's involvement in WWI, and created a one-party communist state." },
  { term: "Stalin", def: "Soviet leader after Lenin who ruled through terror. He industrialized the USSR through brutal Five-Year Plans, collectivized farms (causing famine), and purged millions of people." },
  { term: "Gulag", def: "Soviet forced labor camps where political prisoners and 'enemies of the state' were sent under Stalin. Millions died from harsh conditions." },
  { term: "Soviet Union", def: "The communist state created after the Russian Revolution, officially called the USSR. It was a superpower in the Cold War and collapsed in 1991." },

  // Rise of Fascism & WWII
  { term: "Nazi", def: "Members of Adolf Hitler's National Socialist German Workers' Party. Nazi ideology was based on extreme nationalism, antisemitism, and authoritarianism." },
  { term: "Hitler", def: "Leader of Nazi Germany who rose to power in 1933. He started WWII by invading Poland and orchestrated the Holocaust — the genocide of six million Jews and millions of others." },
  { term: "Lebensraum", def: "German for 'living space.' Hitler's belief that Germany needed to expand eastward to acquire territory for the German people — used to justify aggression against Poland and the USSR." },
  { term: "Nuremberg Laws", def: "Laws passed in Nazi Germany in 1935 that stripped Jews of citizenship and banned marriage between Jews and non-Jews — a key step in institutionalizing antisemitism." },
  { term: "Kristallnacht", def: "'Night of Broken Glass' (November 9–10, 1938) — a coordinated Nazi attack on Jewish homes, businesses, and synagogues. Thousands of Jews were arrested. It marked a major escalation of persecution." },
  { term: "Holocaust", def: "The systematic, state-sponsored genocide of six million Jews and millions of others (Roma, disabled people, political opponents, LGBTQ+ individuals) by the Nazi regime during WWII." },
  { term: "Benito Mussolini", def: "Fascist dictator of Italy who allied with Hitler. He promised to restore Roman-era greatness and used violence (the Black Shirts) to seize power." },
  { term: "Black Shirts", def: "Mussolini's paramilitary force that used violence and intimidation to crush political opposition and help him seize power in Italy in the 1920s." },
  { term: "Fascism", def: "An authoritarian, ultranationalist political ideology that glorifies the state and leader, suppresses opposition, and often relies on violence. Practiced by Mussolini and Hitler." },
  { term: "Hideki Tojo", def: "Japanese military leader and Prime Minister during WWII who oversaw Japanese expansion in Asia and the attack on Pearl Harbor. He was executed as a war criminal after the war." },
  { term: "Japan (WWII)", def: "Sought to build a Pacific empire. Invaded China and Southeast Asia, attacked Pearl Harbor in 1941, and committed atrocities like the Bataan Death March." },
  { term: "Winston Churchill", def: "British Prime Minister during WWII. His leadership and speeches helped Britain resist Nazi Germany during the Blitz. He refused to negotiate with Hitler." },
  { term: "Neville Chamberlain", def: "British PM before Churchill. Known for appeasement — giving Hitler territory (Sudetenland, 1938) to avoid war. It failed and emboldened Hitler." },
  { term: "European Theater", def: "The areas of WWII combat in Europe and North Africa. Key events included D-Day (1944), the Battle of the Bulge, and the fall of Berlin." },
  { term: "Blitzkrieg", def: "German for 'lightning war.' A rapid military strategy using tanks, planes, and infantry in coordinated attacks to overwhelm enemies quickly before they could respond." },
  { term: "Pacific Theater", def: "The areas of WWII combat in the Pacific Ocean and Asia. Key events include Pearl Harbor, island-hopping campaigns, and the use of atomic bombs on Japan." },
  { term: "Bataan Death March", def: "After the fall of the Philippines in 1942, Japanese forces forced 70,000+ American and Filipino POWs to march 65 miles in brutal heat. Thousands died from abuse, starvation, and disease." },
  { term: "Ending the War", def: "WWII ended in Europe on V-E Day (May 8, 1945) after Germany's surrender, and in the Pacific on V-J Day (August 15, 1945) after the US dropped atomic bombs on Hiroshima and Nagasaki." },
  { term: "A-Bomb", def: "The atomic bombs dropped on Hiroshima (Aug. 6, 1945) and Nagasaki (Aug. 9, 1945). Each killed tens of thousands instantly and ended WWII — but opened the nuclear age and debates about civilian targeting." },
  { term: "Repercussions of WWII", def: "WWII reshaped the world: the US and USSR emerged as superpowers, Europe was divided, the UN was created, Israel was founded, the Cold War began, and decolonization accelerated." },

  // Cold War
  { term: "Cold War", def: "A state of geopolitical tension (1947–1991) between the US (capitalism/democracy) and the USSR (communism) that never escalated into direct military conflict but shaped global politics." },
  { term: "Truman Doctrine", def: "President Truman's 1947 policy pledging US support to countries threatened by communist takeover. It was first applied to Greece and Turkey." },
  { term: "Containment", def: "The US foreign policy strategy of preventing communism from spreading to new countries. Shaped US involvement in Korea, Vietnam, and elsewhere during the Cold War." },
  { term: "Marshall Plan", def: "US program (1948) that provided economic aid to rebuild Western European countries after WWII. It aimed to prevent poverty from making communist takeover more appealing." },
  { term: "Berlin Airlift", def: "When the USSR blockaded West Berlin in 1948, the US and Britain flew in supplies for 11 months until the Soviets lifted the blockade. A major early Cold War victory for the West." },
  { term: "Iron Curtain", def: "Churchill's term for the boundary dividing communist Eastern Europe from democratic Western Europe during the Cold War." },
  { term: "Berlin Wall", def: "A wall built by East Germany in 1961 to stop citizens from fleeing to West Berlin. It became the most powerful symbol of Cold War division. It fell in 1989." },
  { term: "NATO", def: "North Atlantic Treaty Organization — a military alliance formed in 1949 by Western nations pledging mutual defense. Created in response to Soviet expansionism." },
  { term: "Mutually Assured Destruction (MAD)", def: "The Cold War doctrine that both the US and USSR had enough nuclear weapons to destroy each other — meaning neither would launch first, because it would guarantee their own annihilation." },
  { term: "Military Industrial Complex", def: "President Eisenhower's term for the powerful relationship between the US military and the defense industry. He warned it could gain undue political influence." },
  { term: "Discrimination", def: "Treating people unfairly based on characteristics like race, gender, or religion. During the Cold War, US racial inequality was used by the USSR as propaganda against American democracy." },
  { term: "Segregation", def: "The forced separation of races, especially in the American South. The Civil Rights Movement fought against legal segregation, culminating in the Civil Rights Act of 1964." },
  { term: "Margaret Thatcher", def: "British Prime Minister (1979–1990) who promoted free-market economics (Thatcherism), reduced government spending, and privatized industries. A major conservative leader of the Cold War era." },
  { term: "GDP (Gross Domestic Product)", def: "The total value of all goods and services produced in a country in a year. Used to measure the size and health of an economy." },
  { term: "Fidel Castro", def: "Communist revolutionary who took control of Cuba in 1959. His alliance with the USSR made Cuba a Cold War flashpoint, especially during the Cuban Missile Crisis." },
  { term: "John F. Kennedy", def: "US President (1961–1963) who navigated the Cuban Missile Crisis, pledged to defend Berlin, and escalated early US involvement in Vietnam before his assassination." },
  { term: "Lyndon B. Johnson", def: "US President after JFK who dramatically escalated the Vietnam War and also passed major civil rights legislation (Civil Rights Act 1964, Voting Rights Act 1965)." },
  { term: "Cuban Missile Crisis", def: "A 13-day standoff in 1962 when the US discovered Soviet nuclear missiles in Cuba. Kennedy and Khrushchev negotiated — the Soviets withdrew missiles, the US promised not to invade Cuba. The closest the Cold War came to nuclear war." },
  { term: "Vietnam War", def: "US military involvement (1955–1975) to prevent communist North Vietnam from taking over South Vietnam. The US withdrew after massive protest and casualties. North Vietnam won." },
  { term: "Tet Offensive", def: "A massive 1968 coordinated attack by North Vietnamese and Viet Cong forces on South Vietnamese cities during the Tet holiday. It shocked Americans who were told the US was winning the war." },
  { term: "Domino Theory", def: "The Cold War belief that if one country fell to communism, neighboring countries would follow like dominoes. Used to justify US involvement in Korea and Vietnam." },
  { term: "Ho Chi Minh", def: "Communist leader of North Vietnam who led the fight to unify Vietnam under communism. He was inspired by nationalism as much as Marxism and is considered a national hero in Vietnam." },
];

const UNITS = [
  { label: "All Terms", filter: null },
  { label: "Enlightenment", filter: (t) => ["Scientific Revolution → Enlightenment","Natural Laws","Social Contract","Hobbes","Locke","Philosophe","Voltaire","Montesquieu","Diderot","Rousseau","Mary Wollstonecraft","Adam Smith","Laissez Faire","Censorship"].includes(t.term) },
  { label: "American & French Revolution", filter: (t) => ["American Revolution","Thomas Jefferson","Declaration of Independence","French Revolution","Louis XVI","Jacques Necker","Marquis de Lafayette","Estates General","Ancien Régime","Deficit Spending","Tennis Court Oath","Storming of the Bastille","The Great Fear","Social Divisions & the Revolution","Reign of Terror","Maximilien Robespierre","Guillotine","Why the Terror Was Allowed","Napoleon","Napoleon's Rise","Napoleonic Code","Concert of Europe"].includes(t.term) },
  { label: "Industrial Revolution", filter: (t) => ["Entrepreneur","Capitalism","Capital","Industrial Revolution","Great Britain (Industrial Rev.)","Luddites","Urbanization","Standard of Living","Communism","Socialism","Tenements","Karl Marx","Textiles","Stocks","Germ Theory"].includes(t.term) },
  { label: "Unification & Imperialism", filter: (t) => ["Zollverein","Otto von Bismarck","Realpolitik","Reich","German Unification","Kulturkampf","Italian Unification","Nationalism in Europe","Failing Empires","Austria-Hungary","New Imperialism","White Man's Burden","Direct Rule","Indirect Rule","Berlin Conference","King Leopold II"].includes(t.term) },
  { label: "WWI", filter: (t) => ["Causes of WWI (MAIN)","Entente","Militarism","Alsace and Lorraine","Mobilize","Neutrality","Stalemate","Schlieffen Plan","Allies (WWI)","Central Powers (WWI)","Trench Warfare","Zeppelin","Total War","Lusitania","Convoy","Conscription","Pandemic","Armistice","Treaty of Versailles","WWI Death Tolls"].includes(t.term) },
  { label: "Interwar & WWII", filter: (t) => ["Collective Security","United Nations","Propaganda","Welfare State","Great Depression","FDR","New Deal","Dust Bowl","Jazz","Russian Revolution","Lenin","Stalin","Gulag","Soviet Union","Nazi","Hitler","Lebensraum","Nuremberg Laws","Kristallnacht","Holocaust","Benito Mussolini","Black Shirts","Fascism","Hideki Tojo","Japan (WWII)","Winston Churchill","Neville Chamberlain","European Theater","Blitzkrieg","Pacific Theater","Bataan Death March","Ending the War","A-Bomb","Repercussions of WWII"].includes(t.term) },
  { label: "Cold War", filter: (t) => ["Cold War","Truman Doctrine","Containment","Marshall Plan","Berlin Airlift","Iron Curtain","Berlin Wall","NATO","Mutually Assured Destruction (MAD)","Military Industrial Complex","Discrimination","Segregation","Margaret Thatcher","GDP (Gross Domestic Product)","Fidel Castro","John F. Kennedy","Lyndon B. Johnson","Cuban Missile Crisis","Vietnam War","Tet Offensive","Domino Theory","Ho Chi Minh"].includes(t.term) },
];

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export default function StudyApp() {
  const [mode, setMode] = useState("menu"); // menu | flashcard | quiz | match
  const [unit, setUnit] = useState(0);
  const [deck, setDeck] = useState([]);
  const [cardIndex, setCardIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [quizQ, setQuizQ] = useState(null);
  const [quizAnswer, setQuizAnswer] = useState(null);
  const [quizScore, setQuizScore] = useState({ correct: 0, total: 0 });
  const [quizDone, setQuizDone] = useState(false);
  const [matchCards, setMatchCards] = useState([]);
  const [matchSelected, setMatchSelected] = useState([]);
  const [matchSolved, setMatchSolved] = useState([]);
  const [matchError, setMatchError] = useState([]);
  const [matchDone, setMatchDone] = useState(false);

  const getTerms = (unitIdx) => {
    const u = UNITS[unitIdx];
    if (!u.filter) return allTerms;
    return allTerms.filter(u.filter);
  };

  const startFlashcard = () => {
    const terms = shuffle(getTerms(unit));
    setDeck(terms);
    setCardIndex(0);
    setFlipped(false);
    setMode("flashcard");
  };

  const startQuiz = () => {
    const terms = shuffle(getTerms(unit));
    setDeck(terms);
    makeQuizQ(terms, 0);
    setQuizScore({ correct: 0, total: 0 });
    setQuizDone(false);
    setMode("quiz");
  };

  const makeQuizQ = (terms, idx) => {
    if (idx >= terms.length) { setQuizDone(true); return; }
    const correct = terms[idx];
    const others = shuffle(allTerms.filter(t => t.term !== correct.term)).slice(0, 3);
    const opts = shuffle([correct, ...others]);
    setQuizQ({ correct, opts, idx });
    setQuizAnswer(null);
  };

  const startMatch = () => {
    const terms = shuffle(getTerms(unit)).slice(0, 6);
    const cards = shuffle([
      ...terms.map((t, i) => ({ id: `t${i}`, text: t.term, pairId: i, type: "term" })),
      ...terms.map((t, i) => ({ id: `d${i}`, text: t.def, pairId: i, type: "def" })),
    ]);
    setMatchCards(cards);
    setMatchSelected([]);
    setMatchSolved([]);
    setMatchError([]);
    setMatchDone(false);
    setMode("match");
  };

  const handleMatchClick = (card) => {
    if (matchSolved.includes(card.id) || matchError.includes(card.id)) return;
    const sel = matchSelected;
    if (sel.includes(card.id)) { setMatchSelected(sel.filter(i => i !== card.id)); return; }
    const newSel = [...sel, card.id];
    setMatchSelected(newSel);
    if (newSel.length === 2) {
      const [a, b] = newSel.map(id => matchCards.find(c => c.id === id));
      if (a.pairId === b.pairId && a.type !== b.type) {
        const newSolved = [...matchSolved, a.id, b.id];
        setMatchSolved(newSolved);
        setMatchSelected([]);
        if (newSolved.length === matchCards.length) setMatchDone(true);
      } else {
        setMatchError([a.id, b.id]);
        setTimeout(() => { setMatchError([]); setMatchSelected([]); }, 900);
      }
    }
  };

  const colors = {
    bg: "#0f1117",
    card: "#1a1d27",
    border: "#2a2d3e",
    accent: "#6c8cff",
    accent2: "#ff6c8c",
    accent3: "#6cffb8",
    text: "#e8eaf6",
    muted: "#7b7f9e",
    success: "#4caf82",
    error: "#ff5c72",
  };

  const styles = {
    app: { minHeight: "100vh", background: colors.bg, color: colors.text, fontFamily: "'IBM Plex Sans', 'Segoe UI', sans-serif", padding: "0" },
    header: { background: colors.card, borderBottom: "1px solid ${colors.border}", padding: "16px 24px", display: "flex", alignItems: "center", justifyContent: "space-between" },
    logo: { fontSize: "18px", fontWeight: "700", letterSpacing: "0.04em", color: colors.accent },
    tag: { fontSize: "11px", background: colors.border, color: colors.muted, padding: "2px 10px", borderRadius: "99px", marginLeft: "10px", fontWeight: "500" },
    body: { maxWidth: "780px", margin: "0 auto", padding: "32px 16px" },
    h1: { fontSize: "28px", fontWeight: "800", marginBottom: "6px" },
    sub: { color: colors.muted, fontSize: "14px", marginBottom: "28px" },
    grid2: { display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: "14px", marginBottom: "24px" },
    unitSelect: { marginBottom: "24px" },
    unitLabel: { fontSize: "12px", color: colors.muted, textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: "8px" },
    unitBtns: { display: "flex", flexWrap: "wrap", gap: "8px" },
    unitBtn: (active) => ({ background: active ? colors.accent : colors.card, color: active ? "#fff" : colors.muted, border: `1px solid ${active ? colors.accent : colors.border}`, borderRadius: "8px", padding: "6px 14px", fontSize: "13px", cursor: "pointer", fontWeight: active ? "600" : "400", transition: "all 0.15s" }),
    modeCard: { background: colors.card, border: `1px solid ${colors.border}`, borderRadius: "14px", padding: "24px", cursor: "pointer", transition: "border-color 0.15s, transform 0.15s" },
    modeIcon: { fontSize: "28px", marginBottom: "10px" },
    modeTitle: { fontSize: "17px", fontWeight: "700", marginBottom: "4px" },
    modeDesc: { fontSize: "13px", color: colors.muted },
    btn: (variant = "primary") => ({
      background: variant === "primary" ? colors.accent : variant === "success" ? colors.success : colors.card,
      color: "#fff",
      border: `1px solid ${variant === "primary" ? colors.accent : variant === "success" ? colors.success : colors.border}`,
      borderRadius: "10px",
      padding: "10px 22px",
      fontSize: "14px",
      fontWeight: "600",
      cursor: "pointer",
      transition: "opacity 0.15s",
    }),
    progress: { color: colors.muted, fontSize: "13px" },
    flashWrap: { perspective: "1000px", cursor: "pointer" },
    flashCard: (f) => ({
      background: colors.card,
      border: `1px solid ${colors.border}`,
      borderRadius: "18px",
      padding: "40px 32px",
      minHeight: "220px",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      textAlign: "center",
      transform: f ? "rotateY(180deg)" : "rotateY(0deg)",
      transition: "transform 0.45s cubic-bezier(.4,0,.2,1)",
      transformStyle: "preserve-3d",
      position: "relative",
    }),
    flashFront: { backfaceVisibility: "hidden", position: "absolute", width: "100%", height: "100%", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: "24px" },
    flashTerm: { fontSize: "22px", fontWeight: "700", color: colors.accent },
    flashHint: { fontSize: "12px", color: colors.muted, marginTop: "12px" },
    flashBack: { backfaceVisibility: "hidden", transform: "rotateY(180deg)", position: "absolute", width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", padding: "24px" },
    flashDef: { fontSize: "15px", lineHeight: "1.65", color: colors.text },
    navRow: { display: "flex", alignItems: "center", gap: "12px", marginTop: "20px", justifyContent: "center" },
    quizCard: { background: colors.card, border: `1px solid ${colors.border}`, borderRadius: "16px", padding: "28px 24px", marginBottom: "20px" },
    quizQ: { fontSize: "17px", fontWeight: "600", marginBottom: "20px", lineHeight: "1.5" },
    quizOpts: { display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" },
    quizOpt: (state) => ({
      background: state === "correct" ? "#1a3a2a" : state === "wrong" ? "#3a1a1a" : "#13151f",
      border: `2px solid ${state === "correct" ? colors.success : state === "wrong" ? colors.error : colors.border}`,
      borderRadius: "10px",
      padding: "12px 16px",
      cursor: state ? "default" : "pointer",
      color: state === "correct" ? colors.success : state === "wrong" ? colors.error : colors.text,
      fontSize: "13px",
      lineHeight: "1.4",
      textAlign: "left",
      transition: "all 0.15s",
      fontWeight: state ? "600" : "400",
    }),
    scoreBox: { background: colors.card, border: `1px solid ${colors.border}`, borderRadius: "16px", padding: "32px", textAlign: "center" },
    scoreNum: { fontSize: "48px", fontWeight: "800", color: colors.accent },
    matchGrid: { display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "10px" },
    matchCard: (state) => ({
      background: state === "solved" ? "#1a2e20" : state === "selected" ? "#1d2240" : state === "error" ? "#2e1a1a" : colors.card,
      border: `2px solid ${state === "solved" ? colors.success : state === "selected" ? colors.accent : state === "error" ? colors.error : colors.border}`,
      borderRadius: "12px",
      padding: "14px 12px",
      cursor: state === "solved" ? "default" : "pointer",
      minHeight: "90px",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      textAlign: "center",
      fontSize: "12px",
      lineHeight: "1.4",
      color: state === "solved" ? colors.success : state === "error" ? colors.error : colors.text,
      transition: "all 0.15s",
      fontWeight: state === "selected" ? "600" : "400",
      opacity: state === "solved" ? 0.5 : 1,
    }),
    backBtn: { background: "transparent", border: "none", color: colors.muted, cursor: "pointer", fontSize: "13px", display: "flex", alignItems: "center", gap: "4px" },
  };

  if (mode === "menu") {
    const termCount = getTerms(unit).length;
    return (
      <div style={styles.app}>
        <div style={styles.header}>
          <div style={{ display: "flex", alignItems: "center" }}>
            <span style={styles.logo}>StudySet</span>
            <span style={styles.tag}>2025 World History Final</span>
          </div>
          <span style={{ fontSize: "13px", color: colors.muted }}>{allTerms.length} total terms</span>
        </div>
        <div style={styles.body}>
          <div style={styles.h1}>Final Exam Review</div>
          <div style={styles.sub}>Choose a unit and study mode to get started.</div>

          <div style={styles.unitSelect}>
            <div style={styles.unitLabel}>Unit</div>
            <div style={styles.unitBtns}>
              {UNITS.map((u, i) => (
                <button key={i} style={styles.unitBtn(unit === i)} onClick={() => setUnit(i)}>{u.label}</button>
              ))}
            </div>
          </div>

          <div style={{ fontSize: "13px", color: colors.muted, marginBottom: "18px" }}>
            {termCount} terms in <strong style={{ color: colors.text }}>{UNITS[unit].label}</strong>
          </div>

          <div style={styles.grid2}>
            <div style={styles.modeCard} onClick={startFlashcard}
              onMouseEnter={e => { e.currentTarget.style.borderColor = colors.accent; e.currentTarget.style.transform = "translateY(-2px)"; }}
              onMouseLeave={e => { e.currentTarget.style.borderColor = colors.border; e.currentTarget.style.transform = ""; }}>
              <div style={styles.modeIcon}>🃏</div>
              <div style={styles.modeTitle}>Flashcards</div>
              <div style={styles.modeDesc}>Flip through all terms and definitions</div>
            </div>
            <div style={styles.modeCard} onClick={startQuiz}
              onMouseEnter={e => { e.currentTarget.style.borderColor = colors.accent2; e.currentTarget.style.transform = "translateY(-2px)"; }}
              onMouseLeave={e => { e.currentTarget.style.borderColor = colors.border; e.currentTarget.style.transform = ""; }}>
              <div style={styles.modeIcon}>📝</div>
              <div style={styles.modeTitle}>Quiz</div>
              <div style={styles.modeDesc}>Multiple choice on every term</div>
            </div>
            <div style={styles.modeCard} onClick={startMatch}
              onMouseEnter={e => { e.currentTarget.style.borderColor = colors.accent3; e.currentTarget.style.transform = "translateY(-2px)"; }}
              onMouseLeave={e => { e.currentTarget.style.borderColor = colors.border; e.currentTarget.style.transform = ""; }}>
              <div style={styles.modeIcon}>🔗</div>
              <div style={styles.modeTitle}>Match</div>
              <div style={styles.modeDesc}>Match 6 terms to their definitions</div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (mode === "flashcard") {
    const card = deck[cardIndex];
    return (
      <div style={styles.app}>
        <div style={styles.header}>
          <button style={styles.backBtn} onClick={() => setMode("menu")}>← Back</button>
          <span style={styles.progress}>{cardIndex + 1} / {deck.length}</span>
        </div>
        <div style={styles.body}>
          <div style={{ marginBottom: "16px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontWeight: "700", fontSize: "16px" }}>Flashcards</span>
            <span style={{ fontSize: "12px", color: colors.muted }}>Click card to flip</span>
          </div>
          <div style={styles.flashWrap} onClick={() => setFlipped(!flipped)}>
            <div style={{ ...styles.flashCard(flipped), minHeight: "240px" }}>
              {!flipped && (
                <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: "10px", width: "100%" }}>
                  <div style={{ fontSize: "11px", color: colors.muted, textTransform: "uppercase", letterSpacing: "0.1em" }}>Term</div>
                  <div style={styles.flashTerm}>{card.term}</div>
                  <div style={styles.flashHint}>Tap to see definition →</div>
                </div>
              )}
              {flipped && (
                <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: "10px", width: "100%", transform: "rotateY(180deg)" }}>
                  <div style={{ fontSize: "11px", color: colors.muted, textTransform: "uppercase", letterSpacing: "0.1em" }}>Definition</div>
                  <div style={styles.flashDef}>{card.def}</div>
                </div>
              )}
            </div>
          </div>
          <div style={styles.navRow}>
            <button style={styles.btn("ghost")} onClick={() => { setCardIndex(Math.max(0, cardIndex - 1)); setFlipped(false); }} disabled={cardIndex === 0}>← Prev</button>
            <button style={styles.btn("primary")} onClick={() => { if (cardIndex < deck.length - 1) { setCardIndex(cardIndex + 1); setFlipped(false); } else setMode("menu"); }}>
              {cardIndex < deck.length - 1 ? "Next →" : "Finish ✓"}
            </button>
          </div>
          <div style={{ marginTop: "20px", background: colors.card, borderRadius: "8px", height: "4px", overflow: "hidden" }}>
            <div style={{ height: "100%", background: colors.accent, width: `${((cardIndex + 1) / deck.length) * 100}%`, transition: "width 0.3s" }} />
          </div>
        </div>
      </div>
    );
  }

  if (mode === "quiz") {
    if (quizDone) return (
      <div style={styles.app}>
        <div style={styles.header}><button style={styles.backBtn} onClick={() => setMode("menu")}>← Back</button></div>
        <div style={styles.body}>
          <div style={styles.scoreBox}>
            <div style={{ fontSize: "14px", color: colors.muted, marginBottom: "8px" }}>Quiz Complete!</div>
            <div style={styles.scoreNum}>{quizScore.correct}/{quizScore.total}</div>
            <div style={{ fontSize: "16px", color: colors.muted, marginTop: "8px", marginBottom: "24px" }}>
              {quizScore.correct === quizScore.total ? "Perfect score! 🎉" : quizScore.correct / quizScore.total >= 0.8 ? "Great job! 🙌" : "Keep studying! 📚"}
            </div>
            <button style={styles.btn("primary")} onClick={startQuiz}>Try Again</button>
          </div>
        </div>
      </div>
    );
    if (!quizQ) return null;
    return (
      <div style={styles.app}>
        <div style={styles.header}>
          <button style={styles.backBtn} onClick={() => setMode("menu")}>← Back</button>
          <span style={styles.progress}>{quizQ.idx + 1} / {deck.length}</span>
        </div>
        <div style={styles.body}>
          <div style={{ marginBottom: "16px", fontWeight: "700" }}>Multiple Choice</div>
          <div style={styles.quizCard}>
            <div style={styles.quizQ}>{quizQ.correct.term}</div>
            <div style={styles.quizOpts}>
              {quizQ.opts.map((opt, i) => {
                let state = null;
                if (quizAnswer !== null) {
                  if (opt.term === quizQ.correct.term) state = "correct";
                  else if (opt.term === quizAnswer && opt.term !== quizQ.correct.term) state = "wrong";
                }
                return (
                  <button key={i} style={styles.quizOpt(state)} onClick={() => {
                    if (quizAnswer !== null) return;
                    setQuizAnswer(opt.term);
                    const correct = opt.term === quizQ.correct.term;
                    setQuizScore(s => ({ correct: s.correct + (correct ? 1 : 0), total: s.total + 1 }));
                    setTimeout(() => makeQuizQ(deck, quizQ.idx + 1), 1000);
                  }}>
                    {opt.def.length > 120 ? opt.def.slice(0, 120) + "…" : opt.def}
                  </button>
                );
              })}
            </div>
          </div>
          <div style={{ background: colors.card, borderRadius: "8px", height: "4px", overflow: "hidden" }}>
            <div style={{ height: "100%", background: colors.accent2, width: `${((quizQ.idx) / deck.length) * 100}%`, transition: "width 0.3s" }} />
          </div>
        </div>
      </div>
    );
  }

  if (mode === "match") {
    return (
      <div style={styles.app}>
        <div style={styles.header}>
          <button style={styles.backBtn} onClick={() => setMode("menu")}>← Back</button>
          <span style={styles.progress}>{matchSolved.length / 2} / 6 matched</span>
        </div>
        <div style={styles.body}>
          <div style={{ marginBottom: "16px", fontWeight: "700" }}>Match the Terms</div>
          {matchDone ? (
            <div style={styles.scoreBox}>
              <div style={{ fontSize: "28px", marginBottom: "8px" }}>🎉</div>
              <div style={{ fontSize: "20px", fontWeight: "700", marginBottom: "16px" }}>All matched!</div>
              <button style={styles.btn("primary")} onClick={startMatch}>Play Again</button>
            </div>
          ) : (
            <div style={styles.matchGrid}>
              {matchCards.map(card => {
                const state = matchSolved.includes(card.id) ? "solved" : matchError.includes(card.id) ? "error" : matchSelected.includes(card.id) ? "selected" : null;
                return (
                  <div key={card.id} style={styles.matchCard(state)} onClick={() => handleMatchClick(card)}>
                    {card.text.length > 80 ? card.text.slice(0, 80) + "…" : card.text}
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    );
  }
}
