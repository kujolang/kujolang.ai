import fs from 'node:fs';
const check = process.argv.includes('--check');
const shell = fs.readFileSync('templates/page-guide.html', 'utf8');
for (const slug of ['language', 'development-workflow', 'performance']) {
  const source = fs.readFileSync(`content/pages/${slug}.md`, 'utf8');
  const body = source.split(/^---\s*$/m).slice(2).join('---').trim();
  const rendered = shell.replace('{{body}}', body);
  const target = `templates/page-guide-${slug}.html`;
  if (check) {
    if (!fs.existsSync(target) || fs.readFileSync(target, 'utf8') !== rendered) throw Error(`Stale guide: ${target}`);
  } else fs.writeFileSync(target, rendered);
}
