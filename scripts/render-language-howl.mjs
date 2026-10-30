import fs from 'node:fs';
const check=process.argv.includes('--check');
const catalog=JSON.parse(fs.readFileSync('examples/catalog.json','utf8'));
const manifest=JSON.parse(fs.readFileSync('howl-social.json','utf8'));
const write=(path,value)=>{if(check){if(!fs.existsSync(path)||fs.readFileSync(path,'utf8')!==value)throw Error(`Stale Howl source: ${path}`);}else fs.writeFileSync(path,value);};
const yaml=fs.readFileSync('content/pages/development-workflow.md','utf8').match(/<code class="language-yaml">([\s\S]*?)<\/code>/)[1];
write('public/samples/development-workflow.yml',yaml+'\n');
const definitions=[
 ['home','Kujo','Programming language for AI-native software.','request-hash'],
 ['examples','Kujo language examples','Code, commands, expected output and pinned sources.','hello-world'],
 ['language','Learn Kujo','Install the runtime and run your first program.','hello-world'],
 ['development-workflow','An inspectable development workflow','Define scope, test changes and inspect the evidence.','development-workflow'],
 ['performance','Performance evidence','Reproduce the measurement and understand its limits.','functions'],
 ...catalog.items.map(x=>['examples-'+x.slug,x.title,x.description,x.slug])
];
const cards=definitions.map(([id,title,tagline,slug])=>{
 const card=manifest.cards.find(x=>x.id===id);if(!card)throw Error(`Missing card: ${id}`);
 const sample=catalog.items.find(x=>x.slug===slug);
 Object.assign(card,{title,tagline,file:`public/samples/${slug}.${slug==='development-workflow'?'yml':'kujo'}`,language:slug==='development-workflow'?'yaml':'kujo',caption:tagline,notes:sample?`Source pinned to ${catalog.commit}. Verification: ${sample.mode}. ${sample.note||''}`:'Configuration example; replace npm test with the existing project test command.'});
 if(sample?.expected)card.expected_output=sample.expected;else delete card.expected_output;
 return card;
});
for(const x of JSON.parse(fs.readFileSync('workflows/catalog.json','utf8')).items){
 const card=manifest.cards.find(c=>c.id==='examples-'+x.slug);
 if(!card)throw Error('Missing workflow card: '+x.slug);
 cards.push(card);
}
write('howl-social.json',JSON.stringify(manifest,null,2)+'\n');
write('howl-language-pages.json',JSON.stringify({...manifest,cards},null,2)+'\n');
console.log(`${check?'Checked':'Updated'} ${cards.length} page showcase sources.`);
