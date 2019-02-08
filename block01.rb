class Robot
  def job
    puts "Started."
    yield
    puts "Finished."
  end
end

robot = Robot.new
robot.job { puts "Hello World!" }
