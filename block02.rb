class Robot
  def initialize(name)
    @name = name
  end
  def job
    puts "Started."
    yield(@name)
    puts "Finished."
  end
end

robot = Robot.new("Alice")
robot.job { |name| puts "Hi, my name is #{name}!" }
