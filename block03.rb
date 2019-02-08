class Robot
  attr_reader :x, :y
  def initialize
    @x = 0
    @y = 0
  end

  def job
    x0, y0 = x, y
    yield(self)
    puts "(#{x0}, #{y0}) => (#{x}, #{y})"
  end

  def move(d1, d2)
    @x += d1
    @y += d2
  end
end

robot = Robot.new

robot.job do |r|
  r.move(1, 0)
  r.move(0, 1)
end

robot.job do |r|
  r.move(1, 0)
  r.move(1, 1)
  r.move(0, -3)
end
