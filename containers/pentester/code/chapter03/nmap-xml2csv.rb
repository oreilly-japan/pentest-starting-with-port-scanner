require 'nmap/xml'
require 'optparse'

nmap_file = ARGV[0]

output_file = 'portscan-result.csv'
opt = OptionParser.new
opt.on('-o', '--output <csv file name>', 'output CSV File') do |val|
  output_file = val
end
opt.on('-h', '--help', 'show help') {
  puts opt
  exit 
}
opt.parse(ARGV)

puts '[+] parse xml file:'
puts nmap_file
puts '-----------------------------------------------------'

result = ''
Nmap::XML.open(nmap_file) do |xml|
  xml.each_host do |host|
    if host.status.to_s == 'up'
      row = false
      host.each_port do |port|
        if port.state.to_s == 'open'
          if !row
            result += host.ip + "\t"
            row = true
          end
          result += "#{port.number}(#{port.service}), "
        end
      end
      if result.end_with?('), ', ')')
        result = result.slice(0...-2)
      end
      if row
        result += "\n"
      end
    end
  end
end
puts result
File.open(output_file, 'w') do |f| 
  f.puts(result)
end

puts '-----------------------------------------------------'
puts '[+] Output: ' + output_file
